#!/usr/bin/python3
"""
Thread-safe circular queue (ring buffer) with blocking put/get semantics.

Combines the O(1) index-arithmetic ring buffer from MyCircularQueue
(LeetCode 622) with the condition-variable-based bounded-blocking-queue
pattern (not_full / not_empty) used in ManualQueue
(spad/rate_limited_task/sync_ratelimited_tasks.py).

Unlike a plain list-backed queue (append + pop(0)), both enqueue and
dequeue here are O(1) — no shifting of remaining elements — because
front/rear are computed via modulo arithmetic over a fixed-size buffer
instead of physically moving items.
"""

import threading
import time

from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")


class ConcurrentCircularQueue(Generic[T]):
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be positive")

        self.buffer: List[Optional[T]] = [None] * capacity
        self.capacity = capacity
        self.size = 0          # number of filled slots
        self.front = 0         # index of the oldest element

        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    # ---- blocking producer/consumer API -----------------------------

    def enqueue(self, value: T, timeout: Optional[float] = None) -> bool:
        """Block until there's room (or timeout elapses), then insert."""
        with self.not_full:
            start_time = time.time()
            while self._is_full():
                if timeout is not None:
                    elapsed = time.time() - start_time
                    remaining = timeout - elapsed
                    if remaining <= 0:
                        return False
                    self.not_full.wait(timeout=remaining)
                else:
                    self.not_full.wait()

            write_index = (self.front + self.size) % self.capacity
            self.buffer[write_index] = value
            self.size += 1
            self.not_empty.notify()
            return True

    def dequeue(self, timeout: Optional[float] = None) -> Optional[T]:
        """Block until an element is available (or timeout elapses)."""
        with self.not_empty:
            start_time = time.time()
            while self._is_empty():
                if timeout is not None:
                    elapsed = time.time() - start_time
                    remaining = timeout - elapsed
                    if remaining <= 0:
                        return None
                    self.not_empty.wait(timeout=remaining)
                else:
                    self.not_empty.wait()

            value = self.buffer[self.front]
            self.buffer[self.front] = None  # drop reference, avoid memory leak
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            self.not_full.notify()
            return value

    # ---- point-in-time queries (snapshot under lock) -----------------

    def front_value(self) -> Optional[T]:
        with self.lock:
            if self._is_empty():
                return None
            return self.buffer[self.front]

    def rear_value(self) -> Optional[T]:
        with self.lock:
            if self._is_empty():
                return None
            rear_index = (self.front + self.size - 1) % self.capacity
            return self.buffer[rear_index]

    def is_empty(self) -> bool:
        with self.lock:
            return self._is_empty()

    def is_full(self) -> bool:
        with self.lock:
            return self._is_full()

    def __len__(self) -> int:
        with self.lock:
            return self.size

    # ---- internal, lock-must-already-be-held helpers ------------------

    def _is_empty(self) -> bool:
        return self.size == 0

    def _is_full(self) -> bool:
        return self.size == self.capacity


if __name__ == "__main__":
    # Quick sanity check: single-threaded behavior should match MyCircularQueue.
    q: ConcurrentCircularQueue[int] = ConcurrentCircularQueue(3)
    assert q.enqueue(1, timeout=0.1)
    assert q.enqueue(2, timeout=0.1)
    assert q.enqueue(3, timeout=0.1)
    assert q.enqueue(4, timeout=0.1) is False  # full, times out
    assert q.rear_value() == 3
    assert q.is_full()
    assert q.dequeue(timeout=0.1) == 1
    assert q.enqueue(4, timeout=0.1)
    assert q.rear_value() == 4
    assert q.front_value() == 2
    print("single-threaded sanity check passed")

    # Producer/consumer smoke test across threads.
    q2: ConcurrentCircularQueue[int] = ConcurrentCircularQueue(5)
    produced = []
    consumed = []
    N = 50

    def producer():
        for i in range(N):
            q2.enqueue(i)
            produced.append(i)

    def consumer():
        for _ in range(N):
            v = q2.dequeue()
            consumed.append(v)

    t_prod = threading.Thread(target=producer)
    t_cons = threading.Thread(target=consumer)
    t_prod.start()
    t_cons.start()
    t_prod.join()
    t_cons.join()

    assert produced == consumed == list(range(N))
    print("producer/consumer smoke test passed")
