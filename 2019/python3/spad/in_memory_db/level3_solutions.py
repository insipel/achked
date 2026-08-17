"""
CodeSignal "In-Memory Database" — Level 3 reference implementation.

Builds on Level 1 (SET / GET / DELETE) and Level 2 (SCAN / SCAN_BY_PREFIX),
adding timestamped operations with TTL (time-to-live) support.

Every Level 3 operation takes a `timestamp` (stringified milliseconds).
Timestamps arrive in strictly increasing order across the whole query
sequence, so the database only ever needs to track each field's *current*
value and (optional) expiration time — never a history of past values.

Level 3 operations (new):
    SET_AT key field value timestamp
        Same as SET, but timestamped. The field never expires (any TTL
        previously set on this field is cleared, since this is a full
        overwrite of the field's state). Returns "".

    SET_AT_WITH_TTL key field value timestamp ttl
        Same as SET_AT, but the field expires at `timestamp + ttl`. Once a
        later operation's timestamp reaches or passes that point, the field
        is treated as if it doesn't exist. Returns "".

    DELETE_AT key field timestamp
        Same as DELETE, but timestamped: removes the field if it currently
        exists and hasn't already expired as of `timestamp`. Returns "true"
        if removed, "false" if the key/field doesn't exist or has expired.

    GET_AT key field timestamp
        Same as GET, but returns "" if the field has expired as of
        `timestamp` (in addition to the usual "record/field missing" case).

    SCAN_AT key timestamp
        Same as SCAN, but only includes fields that haven't expired as of
        `timestamp`.

    SCAN_BY_PREFIX_AT key prefix timestamp
        Same as SCAN_BY_PREFIX, but only includes fields that haven't
        expired as of `timestamp`.

Queries are provided as a list of lists, e.g.:
    ["SET_AT", "A", "B", "E", "1"]
    ["SET_AT_WITH_TTL", "A", "C", "F", "3", "10"]
    ["GET_AT", "A", "C", "12"]

`process_queries` runs a batch of queries and returns the string/list result
of each one (matching CodeSignal's expected output format).
"""

from typing import Dict, List, NamedTuple, Optional


class DBValue(NamedTuple):
    value: str
    expires_at: Optional[int]  # None means "never expires"


class InMemoryDB:
    def __init__(self) -> None:
        # key -> { field -> value }              (Level 1 / 2)
        self._store: Dict[str, Dict[str, str]] = {}
        # key -> { field -> DBValue(value, expires_at) }   (Level 3)
        self._timed_store: Dict[str, Dict[str, DBValue]] = {}

    # ---- Level 1 ----------------------------------------------------

    def set(self, key: str, field: str, value: str) -> str:
        record = self._store.setdefault(key, {})
        record[field] = value
        return ""

    def get(self, key: str, field: str) -> str:
        record = self._store.get(key)
        if record is None:
            return ""
        return record.get(field, "")

    def delete(self, key: str, field: str) -> str:
        record = self._store.get(key)
        if record is None or field not in record:
            return "false"

        del record[field]

        if not record:
            del self._store[key]

        return "true"

    # ---- Level 2 ----------------------------------------------------

    def scan(self, key: str) -> List[str]:
        record = self._store.get(key)
        if not record:
            return []
        return [f"{field}({value})" for field, value in sorted(record.items())]

    def scan_by_prefix(self, key: str, prefix: str) -> List[str]:
        record = self._store.get(key)
        if not record:
            return []
        return [
            f"{field}({value})"
            for field, value in sorted(record.items())
            if field.startswith(prefix)
        ]

    # ---- Level 3 ----------------------------------------------------

    def _live_entry(self, key: str, field: str, timestamp: int) -> Optional[DBValue]:
        """Return field's DBValue if it exists and hasn't expired as of
        `timestamp`; otherwise None. Read-only — does not mutate the store."""
        record = self._timed_store.get(key)
        if record is None:
            return None
        entry = record.get(field)
        if entry is None:
            return None
        if entry.expires_at is not None and timestamp >= entry.expires_at:
            return None
        return entry

    def set_at(self, key: str, field: str, value: str, timestamp: str) -> str:
        record = self._timed_store.setdefault(key, {})
        record[field] = DBValue(value=value, expires_at=None)
        return ""

    def set_at_with_ttl(
        self, key: str, field: str, value: str, timestamp: str, ttl: str
    ) -> str:
        timestamp_i, ttl_i = int(timestamp), int(ttl)
        record = self._timed_store.setdefault(key, {})
        record[field] = DBValue(value=value, expires_at=timestamp_i + ttl_i)
        return ""

    def delete_at(self, key: str, field: str, timestamp: str) -> str:
        timestamp_i = int(timestamp)
        if self._live_entry(key, field, timestamp_i) is None:
            return "false"

        record = self._timed_store[key]
        del record[field]
        if not record:
            del self._timed_store[key]

        return "true"

    def get_at(self, key: str, field: str, timestamp: str) -> str:
        entry = self._live_entry(key, field, int(timestamp))
        return entry.value if entry is not None else ""

    def scan_at(self, key: str, timestamp: str) -> List[str]:
        timestamp_i = int(timestamp)
        record = self._timed_store.get(key)
        if not record:
            return []
        live = [
            (field, entry.value)
            for field, entry in record.items()
            if entry.expires_at is None or timestamp_i < entry.expires_at
        ]
        return [f"{field}({value})" for field, value in sorted(live)]

    def scan_by_prefix_at(self, key: str, prefix: str, timestamp: str) -> List[str]:
        timestamp_i = int(timestamp)
        record = self._timed_store.get(key)
        if not record:
            return []
        live = [
            (field, entry.value)
            for field, entry in record.items()
            if field.startswith(prefix)
            and (entry.expires_at is None or timestamp_i < entry.expires_at)
        ]
        return [f"{field}({value})" for field, value in sorted(live)]


def process_queries(queries: List[List[str]]) -> List[object]:
    db = InMemoryDB()
    results: List[object] = []

    dispatch = {
        "SET": db.set,
        "GET": db.get,
        "DELETE": db.delete,
        "SCAN": db.scan,
        "SCAN_BY_PREFIX": db.scan_by_prefix,
        "SET_AT": db.set_at,
        "SET_AT_WITH_TTL": db.set_at_with_ttl,
        "DELETE_AT": db.delete_at,
        "GET_AT": db.get_at,
        "SCAN_AT": db.scan_at,
        "SCAN_BY_PREFIX_AT": db.scan_by_prefix_at,
    }

    for query in queries:
        op, *args = query
        handler = dispatch.get(op)
        if handler is None:
            raise ValueError(f"Unknown operation: {op}")
        results.append(handler(*args))

    return results


if __name__ == "__main__":
    example_queries = [
        ["SET_AT", "A", "B", "E", "1"],
        ["GET_AT", "A", "B", "2"],
        ["SET_AT_WITH_TTL", "A", "C", "F", "3", "10"],  # expires at 13
        ["GET_AT", "A", "C", "12"],   # still alive (12 < 13)
        ["GET_AT", "A", "C", "13"],   # expired (13 >= 13)
        ["SCAN_AT", "A", "12"],       # both B and C alive
        ["SCAN_AT", "A", "13"],       # only B alive
        ["SET_AT", "A", "C", "G", "14"],  # overwrite clears the old TTL
        ["GET_AT", "A", "C", "1000"],     # never expires now
        ["DELETE_AT", "A", "B", "15"],
        ["DELETE_AT", "A", "B", "16"],    # already gone
        ["SCAN_BY_PREFIX_AT", "A", "B", "20"],
        ["SCAN_BY_PREFIX_AT", "A", "C", "20"],
    ]

    for query, result in zip(example_queries, process_queries(example_queries)):
        print(f"{query} -> {result!r}")
