"""
Level 1 - Basic CRUD
====================

set(key, field, value: int)
    Creates a record with the given key, and adds the given field with the
    given value to the record. If the key + field already exists, update the
    value of the field, incrementing it with the given value.

get(key, field)
    Returns the current value of the field for the given record identified
    by the key. If there's no such key or field present, return None.

delete(key, field)
    Deletes the given field from the record identified by the key. If, after
    deletion, there are no more fields present for the record, remove it
    from storage completely. Return True if any deletion happened,
    otherwise return False.
"""


class InMemoryDBLevel1:
    def __init__(self):
        # key -> {field: value}
        self.db = {}

    def set(self, key, field, value):
        record = self.db.setdefault(key, {})
        record[field] = record.get(field, 0) + value

    def get(self, key, field):
        record = self.db.get(key)
        if record is None:
            return None
        return record.get(field)

    def delete(self, key, field):
        record = self.db.get(key)
        if record is None or field not in record:
            return False

        del record[field]
        if not record:
            del self.db[key]

        return True


if __name__ == "__main__":
    db = InMemoryDBLevel1()
    db.set("A", "count", 1)
    db.set("A", "count", 2)          # count is now 3 (incremented)
    print(db.get("A", "count"))      # 3
    print(db.get("A", "missing"))    # None
    print(db.delete("A", "count"))   # True, record A removed (now empty)
    print(db.get("A", "count"))      # None
    print(db.delete("A", "count"))   # False, nothing to delete
