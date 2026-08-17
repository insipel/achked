"""
LeetCode 981 -- Time Based Key-Value Store.

Design a time-based key-value store that supports:

    set(key, value, timestamp)
        Stores the key with the value at the given time.

    get(key, timestamp)
        Returns a value such that `set` was previously called with
        timestamp_prev <= timestamp. If there are multiple such values,
        returns the one with the largest timestamp_prev. If no such value
        exists, returns "".

Constraints (relevant to the implementation below):
    - Timestamps for `set` calls on the same key are strictly increasing.

Approach:
    Store each key's (timestamp, value) pairs in an append-only list. Since
    `set` calls arrive in strictly increasing timestamp order per key, each
    key's list is already sorted by timestamp -- no need to re-sort on
    read. `get` then binary searches for the rightmost entry whose
    timestamp is <= the query timestamp, exiting early on an exact match
    since timestamps per key are unique.

Complexity:
    set: O(1) amortized.
    get: O(log n) where n is the number of values stored for that key.
    space: O(N) total across all keys.
"""

from collections import defaultdict
from typing import DefaultDict, List, Tuple


class TimeMap:
    def __init__(self) -> None:
        self._store: DefaultDict[str, List[Tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        entries = self._store[key]
        lo, hi = 0, len(entries) - 1
        res = ""

        while lo <= hi:
            mid = (lo + hi) // 2
            mid_ts, mid_val = entries[mid]

            if mid_ts == timestamp:
                return mid_val
            elif mid_ts < timestamp:
                res = mid_val
                lo = mid + 1
            else:
                hi = mid - 1

        return res


if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    print(tm.get("foo", 1))   # "bar"
    print(tm.get("foo", 3))   # "bar"
    tm.set("foo", "bar2", 4)
    print(tm.get("foo", 4))   # "bar2"
    print(tm.get("foo", 5))   # "bar2"
    print(tm.get("baz", 1))   # ""  (key never set)
