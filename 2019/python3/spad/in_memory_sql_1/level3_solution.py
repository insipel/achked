"""
Level 3 - Locking Mechanism
============================

Builds on Level 2 by adding per-record locks so a single "caller" can claim
exclusive write access to a record.

lock(key, caller_id)
    Acquires a lock for the record with the given key, on behalf of
    caller_id.

unlock(key, caller_id)
    Removes the lock from the record with the given key, if it exists and
    was created by the same caller_id.

set_by_caller(key, field, value, caller_id)
    Does the same thing the original set() operation did, but only in case
    there's no lock, or the record is locked by the given caller_id.

delete_by_caller(key, field, caller_id)
    Does the same thing the original delete() operation did, but only in
    case there's no lock, or the record is locked by the given caller_id.

Assumptions made where the prompt is ambiguous (documented so they're easy
to revisit):
  * lock() fails (returns False) if the key doesn't exist yet, or if it is
    already held by ANY caller (including the same caller_id calling lock
    twice in a row) -- locks are not re-entrant.
  * unlock() only succeeds when the lock is currently held by caller_id;
    unlocking a key that isn't locked, or is locked by someone else,
    returns False and has no effect.
  * A record with no active lock behaves exactly like Level 1/2 for
    set_by_caller / delete_by_caller -- any caller_id may mutate it.
"""

from level2_solution import InMemoryDBLevel2


class InMemoryDBLevel3(InMemoryDBLevel2):
    def __init__(self):
        super().__init__()
        # key -> caller_id currently holding the lock
        self.locks = {}

    def lock(self, key, caller_id):
        if key not in self.db:
            return False
        if key in self.locks:
            return False

        self.locks[key] = caller_id
        return True

    def unlock(self, key, caller_id):
        if self.locks.get(key) != caller_id:
            return False

        del self.locks[key]
        return True

    def _is_writable_by(self, key, caller_id):
        holder = self.locks.get(key)
        return holder is None or holder == caller_id

    def set_by_caller(self, key, field, value, caller_id):
        if not self._is_writable_by(key, caller_id):
            return False

        self.set(key, field, value)
        return True

    def delete_by_caller(self, key, field, caller_id):
        if not self._is_writable_by(key, caller_id):
            return False

        return self.delete(key, field)


if __name__ == "__main__":
    db = InMemoryDBLevel3()
    db.set("A", "count", 1)

    print(db.lock("A", "caller1"))                       # True
    print(db.lock("A", "caller2"))                       # False, already locked
    print(db.set_by_caller("A", "count", 5, "caller2"))   # False, blocked by lock
    print(db.set_by_caller("A", "count", 5, "caller1"))   # True, owner can write
    print(db.get("A", "count"))                           # 6
    print(db.unlock("A", "caller2"))                      # False, not the owner
    print(db.unlock("A", "caller1"))                      # True
    print(db.set_by_caller("A", "count", 1, "caller2"))   # True, now unlocked
