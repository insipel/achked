"""
CodeSignal "In-Memory Database" — Level 4 reference implementation.

Builds on Level 1 (SET / GET / DELETE), Level 2 (SCAN / SCAN_BY_PREFIX), and
Level 3 (the timestamped / TTL operations), adding backup and restore.

Level 4 operations (new):
    BACKUP timestamp
        Snapshots the current state of the timestamped store as of
        `timestamp` — only fields that are still alive (not expired) at
        that instant are included. Returns the count of non-empty,
        non-expired *records* (keys) captured in the snapshot, as a string.

    RESTORE timestamp timestamp_to_restore
        Rolls the timestamped store back to the most recent backup taken at
        or before `timestamp_to_restore`. If no such backup exists, the
        store is cleared (there is nothing earlier to restore to). Every
        restored field's remaining TTL (computed relative to the chosen
        backup's own timestamp) is reapplied relative to `timestamp` — the
        moment the RESTORE call itself happens — so a field that had, say,
        16ms left to live at backup time still has 16ms left to live after
        being restored, counted from `timestamp` rather than from its
        original set time. Fields with no TTL remain TTL-free. Returns "".

Design notes:
    - Backups only ever capture the *timestamped* store (the one used by
      SET_AT / GET_AT / etc.). The plain Level 1/2 store has no notion of
      expiration, so it isn't part of what backup/restore reason about.
    - A backup is a snapshot, not a log: only fields alive at the exact
      moment `backup()` is called are captured, and each backup is stored
      independently (a fresh dict), so later mutations to the live store
      never retroactively change an existing backup.

Queries are provided as a list of lists, e.g.:
    ["BACKUP", "5"]
    ["RESTORE", "15", "6"]

`process_queries` runs a batch of queries and returns the string/list result
of each one (matching CodeSignal's expected output format).
"""

from typing import Dict, List, NamedTuple, Optional


class DBValue(NamedTuple):
    value: str
    expires_at: Optional[int]  # None means "never expires"


class InMemoryDB:
    def __init__(self) -> None:
        # key -> { field -> value }                        (Level 1 / 2)
        self._store: Dict[str, Dict[str, str]] = {}
        # key -> { field -> DBValue(value, expires_at) }    (Level 3)
        self._timed_store: Dict[str, Dict[str, DBValue]] = {}
        # backup_timestamp -> { key -> { field -> DBValue } }   (Level 4)
        self._backups: Dict[int, Dict[str, Dict[str, DBValue]]] = {}

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
        # timestamp is accepted for API-shape consistency with the other
        # _at operations; a plain set_at has no expiration to compute.
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

    # ---- Level 4 ----------------------------------------------------

    def backup(self, timestamp: str) -> str:
        timestamp_i = int(timestamp)

        snapshot: Dict[str, Dict[str, DBValue]] = {}
        for key, record in self._timed_store.items():
            live_fields = {
                field: entry
                for field, entry in record.items()
                if entry.expires_at is None or timestamp_i < entry.expires_at
            }
            if live_fields:
                snapshot[key] = live_fields

        self._backups[timestamp_i] = snapshot
        return str(len(snapshot))

    def restore(self, timestamp: str, timestamp_to_restore: str) -> str:
        timestamp_i = int(timestamp)
        target_i = int(timestamp_to_restore)

        eligible = [t for t in self._backups if t <= target_i]
        if not eligible:
            # Nothing was backed up yet at or before the target time.
            self._timed_store = {}
            return ""

        chosen_backup_timestamp = max(eligible)
        snapshot = self._backups[chosen_backup_timestamp]

        restored: Dict[str, Dict[str, DBValue]] = {}
        for key, record in snapshot.items():
            restored_record: Dict[str, DBValue] = {}
            for field, entry in record.items():
                if entry.expires_at is None:
                    new_expires_at = None
                else:
                    remaining_ttl = entry.expires_at - chosen_backup_timestamp
                    new_expires_at = timestamp_i + remaining_ttl
                restored_record[field] = DBValue(
                    value=entry.value, expires_at=new_expires_at
                )
            restored[key] = restored_record

        self._timed_store = restored
        return ""


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
        "BACKUP": db.backup,
        "RESTORE": db.restore,
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
        ["SET_AT_WITH_TTL", "A", "B", "V1", "1", "20"],  # B expires at 21
        ["SET_AT", "A", "C", "V2", "2"],                 # C never expires
        ["BACKUP", "5"],                                 # snapshot #1 @5: B(remaining=16), C
        ["DELETE_AT", "A", "C", "6"],                    # C removed from live store
        ["SET_AT_WITH_TTL", "A", "B", "V1-updated", "7", "5"],  # B now expires at 12
        ["BACKUP", "10"],                                # snapshot #2 @10: B(remaining=2) only
        ["RESTORE", "15", "6"],                          # only snapshot #1 (@5) qualifies (<=6)
        ["GET_AT", "A", "B", "16"],                      # restored: "V1", new expiry 15+16=31
        ["GET_AT", "A", "C", "100"],                     # restored: "V2", never expires
        ["GET_AT", "A", "B", "31"],                      # expired exactly at 31
        ["RESTORE", "50", "1"],                          # no backup at/before t=1 -> cleared
        ["GET_AT", "A", "B", "51"],                      # "" - store was cleared
    ]

    for query, result in zip(example_queries, process_queries(example_queries)):
        print(f"{query} -> {result!r}")
