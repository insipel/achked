#!/usr/bin/python3
"""
Distributed rate limiter (Redis-backed).

This is the "extend it to work in a distributed environment" half of the
rate limiter problem -- the piece token_bucket_rate_limiter.py and
sync_ratelimited_tasks.py (ThreadedRateLimiter) don't cover, since both of
those keep their state (a token count, or a list of timestamps) as a plain
Python object living inside one process's memory.

Why that breaks across multiple servers
-----------------------------------------
Put TokenBucketRateLimiter behind a load balancer with 4 app-server
processes and each process ends up with its own independent bucket. A
client meant to be capped at "2 req/sec" now gets 2 req/sec *per server*
-- 8 req/sec in aggregate -- because no server knows what the others just
admitted. Fixing this means moving the bucket/window state out of process
memory and into a store every server can see: here, Redis.

Why a Lua script instead of separate GET/SET calls
-----------------------------------------------------
The naive port would be: GET state -> compute new value in Python -> SET
state. Two servers hitting the same key at nearly the same time can both
GET the same starting value before either SETs, so both decide "allowed"
when only one unit of capacity actually existed -- a classic
read-modify-write race, just distributed instead of multi-threaded.
redis.call() inside a Lua script is atomic (Redis runs the whole script
single-threaded with no other command interleaved), so the
refill/prune-check-consume sequence below happens as one indivisible step
no matter how many servers call it concurrently. This is the direct
analog of the `self.lock` / `self.rlock` used in the in-process versions
-- just enforced by Redis instead of by a Python threading primitive, so
it works across process and machine boundaries too.

Why redis.call('TIME') instead of time.time() / time.monotonic()
---------------------------------------------------------------------
Each app server has its own clock, and clocks drift across machines.
Computing "elapsed time since last refill" from each server's local clock
would make the decay rate depend on which server happened to handle the
previous request. Reading the time from Redis itself (a single process)
gives every server the same clock for this calculation -- the distributed
equivalent of why the in-process version prefers monotonic() over time().

Per-client keying
--------------------
Both single-process versions enforce one global limit shared by every
caller. A real API rate limiter needs a separate bucket/window per client
(user id, API key, IP, ...), so every method here takes a `client_id` and
maps it to its own Redis key, the same way a real "requests per API key"
limiter would.

Fault tolerance (explicitly called out by ByteByteGo's requirements)
-------------------------------------------------------------------------
If Redis is slow or unreachable, redis-py raises redis.exceptions.RedisError
out of the script call. Callers get to choose fail-open (treat Redis being
down as "admit the request" -- availability over strict enforcement) vs.
fail-closed (treat it as "reject" -- enforcement over availability). This
module does not decide that for you; it lets the exception propagate so the
caller can pick per their own requirements.

Requires: pip install redis, and a reachable Redis server
(defaults to localhost:6379).
"""

import time
import uuid
from concurrent.futures import ThreadPoolExecutor

import redis


class DistributedTokenBucketRateLimiter:
    """Token bucket, one bucket per client_id, state lives in Redis.

    Same algorithm as TokenBucketRateLimiter in token_bucket_rate_limiter.py
    (start full, refill continuously at max_reqs/period tokens per second,
    admit if enough tokens are available) but the bucket -- tokens and
    last_refill -- is a Redis hash instead of instance attributes, and the
    refill-check-consume sequence runs as a single Lua script server-side
    so it stays atomic across every process talking to this Redis instance.
    """

    _SCRIPT = """
    local key = KEYS[1]
    local max_reqs = tonumber(ARGV[1])
    local refill_rate = tonumber(ARGV[2])
    local requested = tonumber(ARGV[3])
    local ttl = tonumber(ARGV[4])

    local time_parts = redis.call('TIME')
    local now = tonumber(time_parts[1]) + tonumber(time_parts[2]) / 1000000

    local bucket = redis.call('HMGET', key, 'tokens', 'last_refill')
    local tokens = tonumber(bucket[1])
    local last_refill = tonumber(bucket[2])

    if tokens == nil then
        -- First request for this client: start full, same as the
        -- in-process version's `self.tokens = float(max_reqs)`.
        tokens = max_reqs
        last_refill = now
    end

    local elapsed = now - last_refill
    if elapsed < 0 then elapsed = 0 end
    tokens = math.min(max_reqs, tokens + elapsed * refill_rate)

    local allowed = 0
    if tokens >= requested then
        tokens = tokens - requested
        allowed = 1
    end

    redis.call('HSET', key, 'tokens', tostring(tokens), 'last_refill', tostring(now))
    -- Let idle clients' keys expire instead of accumulating in Redis forever.
    redis.call('EXPIRE', key, ttl)

    return {allowed, tostring(tokens)}
    """

    def __init__(self, redis_client, max_reqs: int, period: float,
                 key_prefix: str = "ratelimit:tb"):
        if max_reqs <= 0:
            raise ValueError("max_reqs must be positive")
        if period <= 0:
            raise ValueError("period must be positive")

        self.redis = redis_client
        self.max_reqs = max_reqs
        self.period = period
        self.refill_rate = max_reqs / period  # tokens added per second
        self.key_prefix = key_prefix
        # An idle bucket's key gets enough TTL to fully refill, plus slack,
        # then expires on its own -- no separate cleanup job needed.
        self._ttl = int(period) + 2
        self._script = self.redis.register_script(self._SCRIPT)

    def _key(self, client_id: str) -> str:
        return f"{self.key_prefix}:{client_id}"

    def try_admit(self, client_id: str, tokens: int = 1) -> bool:
        """Non-blocking: atomically consume `tokens` for this client if available."""
        allowed, _tokens_left = self._script(
            keys=[self._key(client_id)],
            args=[self.max_reqs, self.refill_rate, tokens, self._ttl],
        )
        return bool(int(allowed))

    def admit(self, client_id: str, tokens: int = 1) -> None:
        """Block until `tokens` are available for this client, then consume them.

        Unlike the in-process version there's no shared lock to hold across
        the sleep: every call to the script below is already an atomic,
        independent round trip to Redis, so any number of processes can be
        polling this same client_id concurrently without stepping on
        each other. Each retry recomputes the wait from the *current*
        server-reported token count, so it self-corrects if another
        process consumed tokens while we were sleeping.
        """
        while True:
            allowed, tokens_left = self._script(
                keys=[self._key(client_id)],
                args=[self.max_reqs, self.refill_rate, tokens, self._ttl],
            )
            if int(allowed):
                return
            deficit = tokens - float(tokens_left)
            wait_time = max(deficit / self.refill_rate, 0.01)
            time.sleep(wait_time)


class DistributedSlidingWindowRateLimiter:
    """Sliding-window-log limiter, one Redis sorted set per client_id.

    Same exact-window semantics as ThreadedRateLimiter in
    sync_ratelimited_tasks.py (no more than max_reqs admits in any
    period-length window, no burst allowance) but the timestamp list is a
    Redis sorted set (score = request time) instead of a Python list
    guarded by self.rlock, and the prune-count-add sequence runs as one
    atomic Lua script per call.

    This also fixes a real bug in ThreadedRateLimiter.admit(): that
    version holds self.rlock across time.sleep(), so only one thread in
    the whole process can be inside admit() at a time -- everyone else
    blocks on the lock, not just on capacity. Here there's no lock held
    across the wait: each attempt is an independent atomic round trip, so
    any number of callers (threads or separate processes) can be polling
    concurrently, the same way the token-bucket class above already fixed
    that for the token-bucket algorithm.
    """

    _SCRIPT = """
    local key = KEYS[1]
    local max_reqs = tonumber(ARGV[1])
    local period = tonumber(ARGV[2])
    local member = ARGV[3]
    local ttl = tonumber(ARGV[4])

    local time_parts = redis.call('TIME')
    local now = tonumber(time_parts[1]) + tonumber(time_parts[2]) / 1000000

    redis.call('ZREMRANGEBYSCORE', key, '-inf', now - period)
    local count = redis.call('ZCARD', key)

    local allowed = 0
    local retry_after = 0
    if count < max_reqs then
        redis.call('ZADD', key, now, member)
        allowed = 1
    else
        local oldest = redis.call('ZRANGE', key, 0, 0, 'WITHSCORES')
        if oldest[2] then
            retry_after = period - (now - tonumber(oldest[2]))
            if retry_after < 0 then retry_after = 0 end
        end
    end
    redis.call('EXPIRE', key, ttl)

    return {allowed, tostring(retry_after)}
    """

    def __init__(self, redis_client, max_reqs: int, period: float,
                 key_prefix: str = "ratelimit:sw"):
        if max_reqs <= 0:
            raise ValueError("max_reqs must be positive")
        if period <= 0:
            raise ValueError("period must be positive")

        self.redis = redis_client
        self.max_reqs = max_reqs
        self.period = period
        self.key_prefix = key_prefix
        self._ttl = int(period) + 2
        self._script = self.redis.register_script(self._SCRIPT)

    def _key(self, client_id: str) -> str:
        return f"{self.key_prefix}:{client_id}"

    @staticmethod
    def _member() -> str:
        # Sorted-set members must be unique per request (two requests can
        # land on the exact same timestamp), so tag each with a random
        # suffix rather than relying on the timestamp alone.
        return f"{time.time()}:{uuid.uuid4().hex}"

    def try_admit(self, client_id: str) -> bool:
        """Non-blocking: atomically admit this client's request if the window allows it."""
        allowed, _retry_after = self._script(
            keys=[self._key(client_id)],
            args=[self.max_reqs, self.period, self._member(), self._ttl],
        )
        return bool(int(allowed))

    def admit(self, client_id: str) -> None:
        """Block until the sliding window has room for this client, then admit."""
        while True:
            allowed, retry_after = self._script(
                keys=[self._key(client_id)],
                args=[self.max_reqs, self.period, self._member(), self._ttl],
            )
            if int(allowed):
                return
            time.sleep(max(float(retry_after), 0.01))


if __name__ == "__main__":
    # Demo: prove the limiter caps traffic in *aggregate* across multiple
    # independent Redis connections standing in for separate app-server
    # processes -- each one has its own Python object and no shared
    # in-process state, only the same Redis instance, which is the whole
    # point of this file vs. the single-process versions.
    client = redis.Redis(host="localhost", port=6379, decode_responses=True)
    try:
        client.ping()
    except redis.exceptions.ConnectionError as exc:
        raise SystemExit(
            "Couldn't reach Redis on localhost:6379 -- start one first "
            "(e.g. `redis-server`) before running this demo."
        ) from exc

    print("=== Token bucket: 4 simulated servers, one client, capped at 2 req/sec ===")
    # Each "server" gets its own Redis connection, not just its own Python
    # object -- that's the point being demoed: these 4 limiters share no
    # Python state whatsoever (unlike 4 instances of TokenBucketRateLimiter,
    # which would each keep their own independent in-memory bucket), only
    # the same Redis-side key.
    tb_limiters = [
        DistributedTokenBucketRateLimiter(
            redis.Redis(host="localhost", port=6379, decode_responses=True),
            max_reqs=2, period=1.0,
        )
        for _ in range(4)
    ]
    start = time.monotonic()
    print_lock = __import__("threading").Lock()

    def tb_worker(server_id: int, limiter: DistributedTokenBucketRateLimiter, num_calls: int):
        for i in range(num_calls):
            limiter.admit("client-A")
            elapsed = time.monotonic() - start
            with print_lock:
                print(f"server[{server_id}] admitted call {i} at t={elapsed:.2f}s")

    # Enumerate produces (1, tb_limiters[0]), (2, tb_limiters[1]),
    # (3, tb_limiters[2]), (4, tb_limiters[3]).
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(tb_worker, sid, lim, 3)
                   for sid, lim in enumerate(tb_limiters, start=1)]
        for f in futures:
            f.result()

    total_elapsed = time.monotonic() - start
    print(f"---- 12 calls across 4 servers admitted in {total_elapsed:.2f}s "
          f"(expected roughly {12 / 2 - 1:.1f}s+ after the initial burst, "
          f"same as the single-process demo -- proving the cap held "
          f"in aggregate even though no server shares Python state) ----\n")

    print("=== Sliding window: two different clients don't interfere ===")
    sw_limiter = DistributedSlidingWindowRateLimiter(client, max_reqs=2, period=1.0)
    for client_id in ("client-A", "client-B"):
        results = [sw_limiter.try_admit(client_id) for _ in range(3)]
        print(f"{client_id}: try_admit x3 -> {results} (expect [True, True, False])")
