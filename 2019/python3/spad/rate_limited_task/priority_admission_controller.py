#!/usr/bin/python3
"""
Priority-tiered admission controller (concurrency limiter, not a rate limiter).

This is the "second layer" from the admission-control discussion: the
piece a rate limiter (token_bucket_rate_limiter.py, sync_ratelimited_tasks.py,
distributed_rate_limiter.py) structurally can't do, because a rate limiter
only answers "has this client exceeded N requests in a time window?" -- it
has no notion of how much work is *currently in flight* against the
system's actual capacity, and no notion of request priority.

What this answers instead: "how many requests are being processed right
now, and if we're at capacity, whose requests get shed first?" That's a
concurrency question (how many are in progress), not a rate question (how
many arrived per second), and it's what protects the system when many
different well-behaved clients -- each individually within their own rate
limit -- still add up to more concurrent load than the system can handle.

Why a semaphore per tier, not a mutex
-----------------------------------------
A mutex enforces exclusivity: exactly one holder at a time. Reserved
capacity isn't an exclusivity problem, it's a counting problem -- "let up
to K critical requests run concurrently, block/reject the (K+1)th." A
mutex can only express K=1; using one to guard a tier's pool would cap
that tier at a single concurrent request no matter how much capacity was
meant to be reserved for it, turning the protection mechanism itself into
an artificial bottleneck. A semaphore generalizes a mutex to K permits
(Semaphore(1) == a mutex), which is exactly the primitive "reserve N
concurrent slots for this tier" needs.

Why one semaphore *per tier* instead of one shared semaphore
------------------------------------------------------------------
A single shared semaphore for the whole system would let a flood of
low-priority traffic exhaust all the permits before any critical request
arrives -- there's no isolation. Giving each tier its own semaphore with
its own fixed permit count means best-effort traffic saturating its pool
can never take a slot away from critical traffic's pool: the two tiers
are isolated by construction, not by ordering or scheduling tricks. The
trade-off is that a reserved slot sits idle if that tier is quiet and
another tier is overloaded -- this "small version" intentionally takes
that trade-off for simplicity; a fuller design could add a shared
overflow pool that any tier may borrow from when its own pool is full, in
priority order, with critical still preferring its private reservation
first.

How this composes with the rate limiter layer
-------------------------------------------------
In a full request path, the per-client rate limiter (are you sending more
than *you're* allowed to?) runs first, closer to the client/edge; this
concurrency limiter (is the system able to take on more work *right now*,
and if not, whose work matters more?) runs second, closer to the actual
resource being protected. A request can pass the rate limiter and still
be shed here if the system is genuinely overloaded -- that's the case a
rate limiter alone can never catch.
"""

import threading
import time
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from typing import Dict, Optional


class AdmissionRejected(Exception):
    """Raised when a request is shed because its tier is at capacity."""

    def __init__(self, tier: str):
        self.tier = tier
        super().__init__(f"admission rejected: tier '{tier}' is at capacity")


class PriorityConcurrencyLimiter:
    """Caps concurrent in-flight work per priority tier.

    Each tier gets its own threading.Semaphore, initialized with that
    tier's reserved permit count. Tiers are isolated: exhausting one
    tier's permits has no effect on any other tier's.
    """

    def __init__(self, capacity_by_tier: Dict[str, int]):
        if not capacity_by_tier:
            raise ValueError("capacity_by_tier must not be empty")
        for tier, capacity in capacity_by_tier.items():
            if capacity <= 0:
                raise ValueError(f"capacity for tier '{tier}' must be positive")

        self.capacity_by_tier = dict(capacity_by_tier)
        self._semaphores = {
            tier: threading.Semaphore(capacity)
            for tier, capacity in capacity_by_tier.items()
        }
        # In-flight counters purely for observability/demo output -- a
        # Semaphore doesn't expose "how many permits are currently held",
        # only acquire/release, so we track this ourselves.
        self._in_flight = {tier: 0 for tier in capacity_by_tier}
        self._in_flight_lock = threading.Lock()

    def _tier_semaphore(self, tier: str) -> threading.Semaphore:
        try:
            return self._semaphores[tier]
        except KeyError:
            raise ValueError(f"unknown tier '{tier}', expected one of {list(self._semaphores)}")

    def try_admit(self, tier: str) -> bool:
        """Non-blocking: reserve a slot in `tier`'s pool if one's free."""
        sem = self._tier_semaphore(tier)
        acquired = sem.acquire(blocking=False)
        if acquired:
            with self._in_flight_lock:
                self._in_flight[tier] += 1
        return acquired

    def admit(self, tier: str, timeout: Optional[float] = None) -> bool:
        """Block (up to `timeout` seconds, or forever if None) for a free slot.

        Returns True if admitted, False if the wait timed out. Unlike the
        rate limiters' admit(), there's no "recompute a wait time and
        sleep" loop needed -- Semaphore.acquire() already blocks
        efficiently (via a condition variable) until another holder
        releases, rather than polling.
        """
        sem = self._tier_semaphore(tier)
        acquired = sem.acquire(blocking=True, timeout=timeout)
        if acquired:
            with self._in_flight_lock:
                self._in_flight[tier] += 1
        return acquired

    def release(self, tier: str) -> None:
        """Return a previously-acquired slot to `tier`'s pool."""
        with self._in_flight_lock:
            self._in_flight[tier] -= 1
        self._tier_semaphore(tier).release()

    @contextmanager
    def admission(self, tier: str):
        """Context-manager form: raises AdmissionRejected if the tier is full.

        Usage:
            with limiter.admission("critical"):
                handle_request(...)
        """
        if not self.try_admit(tier):
            raise AdmissionRejected(tier)
        '''
        >>> how is try/yield/finally used here?
        This is the standard @contextmanager pattern from contextlib,
        and try/finally here is doing one specific, important job:
        guaranteeing the semaphore permit always gets returned, even if
        something goes wrong inside the with block.

        Walking through what happens when someone writes with
        limiter.admission("critical"): handle_request(...):

        The @contextmanager decorator turns this generator function into
        something usable with with. Everything before yield runs on entry —
        that's try_admit(tier), which acquires a permit or raises
        AdmissionRejected if the tier's full. The yield statement is the
        handoff point: control passes to whatever code is inside the caller's
        with block (handle_request(...)), and the generator function is paused
        right there, sitting on that line. Everything after yield runs on exit
        from the with block — that's self.release(tier).

        The finally is what makes this safe rather than just convenient. Without
        it, if handle_request(...) throws an exception, execution would jump
        straight out of the generator function without ever reaching
        self.release(tier) — the permit would never go back to the semaphore.
        That's a permanent leak: this tier's effective capacity silently
        shrinks by one every time a request errors out.
        '''
        try:
            yield
        finally:
            self.release(tier)

    def in_flight(self, tier: str) -> int:
        with self._in_flight_lock:
            return self._in_flight[tier]


if __name__ == "__main__":
    # Demo: prove tier isolation -- flood "best_effort" past its capacity
    # (so it starts shedding) at the same time as "critical" traffic is
    # sent at a rate under critical's own reserved capacity, and confirm
    # best_effort saturating its pool has zero effect on critical's
    # admit rate.
    limiter = PriorityConcurrencyLimiter({"critical": 3, "best_effort": 2})
    print_lock = threading.Lock()

    def hold_slot(tier: str, request_id: int, hold_seconds: float, results: list):
        try:
            with limiter.admission(tier):
                with print_lock:
                    print(f"[{tier}] req {request_id} ADMITTED "
                          f"(in_flight={limiter.in_flight(tier)}/{limiter.capacity_by_tier[tier]})")
                results.append((tier, request_id, "admitted"))
                time.sleep(hold_seconds)
        except AdmissionRejected:
            with print_lock:
                print(f"[{tier}] req {request_id} REJECTED (tier at capacity)")
            results.append((tier, request_id, "rejected"))

    results = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = []
        # Flood best_effort with 6 requests against a reserved pool of 2 --
        # this tier should end up mostly shedding.
        for i in range(6):
            futures.append(executor.submit(hold_slot, "best_effort", i, 0.3, results))
        # Send 3 critical requests against a reserved pool of 3 -- all of
        # these should be admitted regardless of how saturated
        # best_effort is, because the pools are isolated.
        for i in range(3):
            futures.append(executor.submit(hold_slot, "critical", i, 0.3, results))
        for f in futures:
            f.result()

    critical_admitted = sum(1 for t, _, r in results if t == "critical" and r == "admitted")
    best_effort_admitted = sum(1 for t, _, r in results if t == "best_effort" and r == "admitted")
    print(f"\n---- critical: {critical_admitted}/3 admitted (expect 3/3 -- untouched by "
          f"best_effort's overload) | best_effort: {best_effort_admitted}/6 admitted "
          f"(expect 2/6 concurrently, rest shed) ----")
