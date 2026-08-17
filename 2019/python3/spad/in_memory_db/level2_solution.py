"""
CodeSignal "In-Memory Database" — Level 2 reference implementation.

Builds on Level 1 (SET / GET / DELETE) and adds scanning operations.

Level 1 operations (unchanged):
    SET key field value
        Inserts a field-value pair into the record associated with `key`.
        If the field already exists, its value is replaced. If the record
        does not exist, it is created. Returns "".

    GET key field
        Returns the value contained within `field` of the record associated
        with `key`. If the record or the field does not exist, returns "".

    DELETE key field
        Removes `field` from the record associated with `key`. Returns
        "true" if the field was successfully deleted, "false" if the key or
        field does not exist.

Level 2 operations (new):
    SCAN key
        Returns all field-value pairs of the record associated with `key`
        as strings formatted "field(value)", sorted lexicographically by
        field name. Returns an empty list if the record doesn't exist.

    SCAN_BY_PREFIX key prefix
        Same as SCAN, but only includes fields that start with `prefix`.

Queries are provided as a list of lists, e.g.:
    ["SET", "A", "B", "E"]
    ["SCAN", "A"]
    ["SCAN_BY_PREFIX", "A", "B"]

`process_queries` runs a batch of queries and returns the string/list result
of each one (matching CodeSignal's expected output format).
"""

from typing import Dict, List


class InMemoryDB:
    def __init__(self) -> None:
        # key -> { field -> value }
        self._store: Dict[str, Dict[str, str]] = {}

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

        # Clean up empty records (not required by the spec, but tidy).
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


def process_queries(queries: List[List[str]]) -> List[object]:
    db = InMemoryDB()
    results: List[object] = []

    dispatch = {
        "SET": db.set,
        "GET": db.get,
        "DELETE": db.delete,
        "SCAN": db.scan,
        "SCAN_BY_PREFIX": db.scan_by_prefix,
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
        ["SET", "A", "BC", "E"],
        ["SET", "A", "BD", "F"],
        ["SET", "A", "C", "G"],
        ["SCAN", "A"],
        ["SCAN_BY_PREFIX", "A", "B"],
        ["SCAN_BY_PREFIX", "A", "Z"],
        ["SCAN", "X"],
        ["DELETE", "A", "BC"],
        ["SCAN", "A"],
    ]

    for query, result in zip(example_queries, process_queries(example_queries)):
        print(f"{query} -> {result!r}")
