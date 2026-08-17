"""
Level 4 - Advanced Operations
===============================

Builds on Level 3 with two more operations.

logout(caller_id)
    Releases all the locks acquired by the given caller_id. Returns the
    number of locks released.

undo(key, caller_id)
    For a record that is currently locked by the given caller_id, resets it
    to the state (all fields, values) it was in before the lock was
    acquired.

Assumptions made where the prompt is ambiguous:
  * undo() only has an effect while the lock is still held by caller_id; if
    the record isn't locked by that caller, it returns False and does
    nothing.
  * undo() restores field/value state but does NOT release the lock --
    callers can keep editing (or unlock explicitly) afterwards.
  * undo() is idempotent: calling it twice in a row leaves the record in the
    same "pre-lock" state both times.
  * If the record didn't exist before the lock was acquired (lock() itself
    only succeeds on existing keys per Level 3, so this is mostly
    theoretical), undo would remove the record entirely.
"""

from level3_solution import InMemoryDBLevel3


class InMemoryDBLevel4(InMemoryDBLevel3):
    def __init__(self):
        super().__init__()
        # key -> snapshot of its fields dict, taken at the moment lock()
        # succeeded, so undo() can restore it later.
        self.pre_lock_snapshots = {}

    def lock(self, key, caller_id):
        acquired = super().lock(key, caller_id)
        if acquired:
            self.pre_lock_snapshots[key] = dict(self.db.get(key, {}))
        return acquired

    def unlock(self, key, caller_id):
        released = super().unlock(key, caller_id)
        if released:
            self.pre_lock_snapshots.pop(key, None)
        return released

    def logout(self, caller_id):
        keys_held = [key for key, owner in self.locks.items() if owner == caller_id]
        for key in keys_held:
            del self.locks[key]
            self.pre_lock_snapshots.pop(key, None)
        return len(keys_held)

    def undo(self, key, caller_id):
        if self.locks.get(key) != caller_id:
            return False
        if key not in self.pre_lock_snapshots:
            return False

        original_fields = self.pre_lock_snapshots[key]
        if original_fields:
            self.db[key] = dict(original_fields)
        else:
            self.db.pop(key, None)

        return True


if __name__ == "__main__":
    db = InMemoryDBLevel4()
    db.set("A", "count", 1)
    db.set("A", "name", 10)  # arbitrary numeric field

    db.lock("A", "caller1")
    db.set_by_caller("A", "count", 100, "caller1")
    print(db.get("A", "count"))          # 101

    print(db.undo("A", "caller1"))       # True
    print(db.get("A", "count"))          # 1, back to pre-lock state

    print(db.logout("caller1"))          # 1, released A's lock
    print(db.unlock("A", "caller1"))     # False, no longer locked
