"""
CodeSignal "In-Memory Database" — Level 1 reference implementation.

Level 1 operations:
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

Queries are provided as a list of lists, e.g.:
    ["SET", "A", "B", "E"]
    ["GET", "A", "B"]
    ["DELETE", "A", "B"]

`process_queries` runs a batch of queries and returns the string result of
each one (matching CodeSignal's expected output format).
"""

from typing import Dict, List


class InMemoryDB:
    def __init__(self) -> None:
        # key -> { field -> value }
        self._store: Dict[str, Dict[str, str]] = {}

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


def process_queries(queries: List[List[str]]) -> List[str]:
    db = InMemoryDB()
    results: List[str] = []

    dispatch = {
        "SET": db.set,
        "GET": db.get,
        "DELETE": db.delete,
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
        ["SET", "A", "B", "E"],
        ["GET", "A", "B"],
        ["GET", "A", "C"],
        ["SET", "A", "C", "F"],
        ["SET", "A", "B", "G"],
        ["GET", "A", "B"],
        ["DELETE", "A", "B"],
        ["DELETE", "A", "B"],
        ["GET", "A", "B"],
        ["GET", "X", "Y"],
    ]

    for query, result in zip(example_queries, process_queries(example_queries)):
        print(f"{query} -> {result!r}")
