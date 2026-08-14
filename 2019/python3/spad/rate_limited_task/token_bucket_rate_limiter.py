#!/usr/bin/python3
"""
Token-bucket rate limiter.

Compared to the sliding-window-log approach in sync_ratelimited_tasks.py
(ThreadedRateLimiter), this version:
  - stores O(1) state (a token count + a last-refill timestamp) instead of
    a growing/shrinking list of every request timestamp in the window, so
    admit() is O(1) per call instead of O(n) in stored timestamps.
  - never holds its lock across time.sleep(): it computes how long to wait,
    releases the lock, sleeps, then reacquires and rechecks. Other threads
    can make progress (consume tokens, refill) while one thread is sleeping.
  - uses time.monotonic() instead of time.time() for interval math, since
    time.time() can jump backwards/forwards on NTP sync or manual clock
    changes, which would corrupt elapsed-time calculations.

Trade-off vs. the sliding-window log: token bucket allows short bursts up
to `max_reqs` tokens (e.g. if idle, you can fire `max_reqs` requests
instantly), whereas a sliding-window log enforces an exact "no more than
max_reqs in any period-length window" with no burst allowance. In exchange
you get O(1) memory/time instead of O(n).
"""

import threading
import time
from concurrent.futures import ThreadPoolExecutor


class TokenBucketRateLimiter:
    def __init__(self, max_reqs: int, period: float):
        if max_reqs <= 0:
            raise ValueError("max_reqs must be positive")
        if period <= 0:
            raise ValueError("period must be positive")

        self.max_reqs = max_reqs
        self.period = period
        self.refill_rate = max_reqs / period  # tokens added per second

        self.tokens = float(max_reqs)  # start full: allow an initial burst
        self.last_refill = time.monotonic()
        self.lock = threading.Lock()

    def _refill_locked(self) -> None:
        """Top up tokens based on elapsed time. Caller must hold self.lock."""
        now = time.monotonic()
        elapsed = now - self.last_refill
        if elapsed > 0:
            self.tokens = min(self.max_reqs, self.tokens + elapsed * self.refill_rate)
            self.last_refill = now

    def admit(self) -> None:
        """Block until a token is available, then consume one."""
        while True:
            with self.lock:
                self._refill_locked()
                if self.tokens >= 1:
                    self.tokens -= 1
                    return
                deficit = 1 - self.tokens
                wait_time = deficit / self.refill_rate
            # Lock released here -- other threads aren't blocked while we sleep.
            time.sleep(wait_time)
            # Loop back around: reacquire, refill, and recheck. Don't assume
            # the token we waited for is still ours -- another thread may
            # have grabbed it first.

    def try_admit(self) -> bool:
        """Non-blocking: consume a token if one's available, else return False."""
        with self.lock:
            self._refill_locked()
            if self.tokens >= 1:
                self.tokens -= 1
                return True
            return False


if __name__ == "__main__":
    # Demo: 4 threads all hammering a limiter capped at 2 requests/second.
    # Expect roughly 2 admits per 1-second window, after an initial burst
    # of up to `max_reqs` since the bucket starts full.
    limiter = TokenBucketRateLimiter(max_reqs=2, period=1.0)
    start = time.monotonic()
    lock = threading.Lock()

    def worker(worker_id: int, num_calls: int):
        for i in range(num_calls):
            limiter.admit()
            elapsed = time.monotonic() - start
            with lock:
                print(f"worker[{worker_id}] admitted call {i} at t={elapsed:.2f}s")

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(worker, wid, 3) for wid in range(1, 5)]
        for f in futures:
            f.result()

    total_elapsed = time.monotonic() - start
    print(f"---- done: 12 calls admitted in {total_elapsed:.2f}s "
          f"(expected roughly {12 / 2 - 1:.1f}s+ after the initial burst) ----")
