"""
Level 2 - Modification Tracking
================================

Builds on Level 1 by tracking how many times each key has been modified.

get_top_n_modified(n)
    Returns a list of strings of the top-n records in the format
    "key(modifications_qty)", sorted by number of modifications made on that
    key so far, with ties broken alphabetically by key (ascending).

    A modification is any of: inserting a new record, inserting a field,
    updating a field's value, or deleting a field. If a record is completely
    removed from the database (its last field was deleted), it is excluded
    from consideration entirely -- its modification history is dropped.
"""

from level1_solution import InMemoryDBLevel1


class InMemoryDBLevel2(InMemoryDBLevel1):
    def __init__(self):
        super().__init__()
        # key -> number of modifications made to that key
        self.modifications = {}

    def set(self, key, field, value):
        super().set(key, field, value)
        self.modifications[key] = self.modifications.get(key, 0) + 1

    def delete(self, key, field):
        deleted = super().delete(key, field)
        if not deleted:
            return False

        self.modifications[key] = self.modifications.get(key, 0) + 1

        # Record was fully removed -> drop it from consideration entirely.
        if key not in self.db:
            del self.modifications[key]

        return deleted

    def get_top_n_modified(self, n):
        ranked = sorted(
            self.modifications.items(),
            key=lambda item: (-item[1], item[0]),
        )
        return [f"{key}({count})" for key, count in ranked[:n]]


if __name__ == "__main__":
    db = InMemoryDBLevel2()
    db.set("A", "count", 1)   # A: 1 modification
    db.set("A", "count", 2)   # A: 2 modifications
    db.set("B", "count", 1)   # B: 1 modification
    db.set("C", "count", 1)   # C: 1 modification
    print(db.get_top_n_modified(3))   # ['A(2)', 'B(1)', 'C(1)']  (tie -> alphabetical)

    db.delete("A", "count")   # A had only one field -> record fully removed
    print(db.get_top_n_modified(3))   # ['B(1)', 'C(1)']  (A dropped entirely)
