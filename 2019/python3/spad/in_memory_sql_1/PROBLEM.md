# In-Memory Database: Implement SQL-Like Operations

Source: [Hello Interview](https://www.hellointerview.com/community/questions/memory-database-sql/cmbsl00wk004v07adwuorveqo)
(reported as a CodeSignal assessment used by Anthropic; must be done in Python.)

## Level 1 — Basic CRUD

- `set(key, field, value: int)` — Creates a record with the given key, and adds the given
  field with the given value to the record. If the key + field already exists, update the
  value of the field, incrementing it with the given value.
- `get(key, field)` — Returns the current value of the field for the given record identified
  by the key. If there's no such key or field present, return `None`.
- `delete(key, field)` — Deletes the given field from the record identified by the key. If,
  after deletion, there are no more fields present for the record, remove it from storage
  completely. Return `True` if any deletion happened, otherwise `False`.

## Level 2 — Modification Tracking

- `get_top_n_modified(n)` — Returns a list of strings of the top-n records in the format
  `"key(modifications_qty)"`, sorted by number of modifications made on that key, ties broken
  alphabetically. A modification is: insert of a record, insert of a field, a field's value
  update, or a field deletion. If a record is completely removed from the database, it's also
  removed from consideration.

## Level 3 — Locking Mechanism

- `lock(key, caller_id)` — Acquires a lock for the record with the given key by the caller_id.
- `unlock(key, caller_id)` — Removes the lock from the record with the given key, if it exists
  and was created by the same caller_id.
- `set_by_caller(key, field, value: int, caller_id)` — Same as `set`, but only in case there's
  no lock or it's locked by the given caller_id.
- `delete_by_caller(key, field, caller_id)` — Same as `delete`, but only in case there's no
  lock or it's locked by the given caller_id.

## Level 4 — Advanced Operations

- `logout(caller_id)` — Releases all the locks acquired by the given caller_id. Returns the
  number of released locks.
- `undo(key, caller_id)` — For a record currently locked by the given caller_id, reset it to
  the state (all fields, values) it was in before the lock was acquired.

## Files

- `level1_solution.py` — Level 1 (`InMemoryDBLevel1`)
- `level2_solution.py` — Level 2, extends Level 1 (`InMemoryDBLevel2`)
- `level3_solution.py` — Level 3, extends Level 2 (`InMemoryDBLevel3`)
- `level4_solution.py` — Level 4, extends Level 3 (`InMemoryDBLevel4`)
- `test_solution.py` — unittest suite covering all four levels (26 tests, all passing)

Each level file has a `__main__` block with a small runnable demo. Ambiguous edge cases
(e.g. locking a non-existent key, double-locking, whether `undo` releases the lock) are
documented as explicit assumptions in each file's docstring, since the original prompt
doesn't spell them out.
