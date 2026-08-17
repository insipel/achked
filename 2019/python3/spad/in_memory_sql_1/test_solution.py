import unittest

from level1_solution import InMemoryDBLevel1
from level2_solution import InMemoryDBLevel2
from level3_solution import InMemoryDBLevel3
from level4_solution import InMemoryDBLevel4


class TestLevel1(unittest.TestCase):
    def setUp(self):
        self.db = InMemoryDBLevel1()

    def test_set_and_get(self):
        self.db.set("A", "count", 1)
        self.assertEqual(self.db.get("A", "count"), 1)

    def test_set_increments_existing_field(self):
        self.db.set("A", "count", 1)
        self.db.set("A", "count", 4)
        self.assertEqual(self.db.get("A", "count"), 5)

    def test_get_missing_key_or_field_returns_none(self):
        self.assertIsNone(self.db.get("missing", "field"))
        self.db.set("A", "count", 1)
        self.assertIsNone(self.db.get("A", "other_field"))

    def test_delete_field_returns_true(self):
        self.db.set("A", "x", 1)
        self.db.set("A", "y", 2)
        self.assertTrue(self.db.delete("A", "x"))
        self.assertIsNone(self.db.get("A", "x"))
        self.assertEqual(self.db.get("A", "y"), 2)

    def test_delete_last_field_removes_record(self):
        self.db.set("A", "x", 1)
        self.assertTrue(self.db.delete("A", "x"))
        self.assertNotIn("A", self.db.db)

    def test_delete_missing_returns_false(self):
        self.assertFalse(self.db.delete("A", "x"))
        self.db.set("A", "x", 1)
        self.assertFalse(self.db.delete("A", "y"))


class TestLevel2(unittest.TestCase):
    def setUp(self):
        self.db = InMemoryDBLevel2()

    def test_set_counts_as_modification(self):
        self.db.set("A", "x", 1)
        self.db.set("A", "x", 1)
        self.db.set("B", "x", 1)
        self.assertEqual(self.db.get_top_n_modified(2), ["A(2)", "B(1)"])

    def test_ties_broken_alphabetically(self):
        self.db.set("C", "x", 1)
        self.db.set("B", "x", 1)
        self.db.set("A", "x", 1)
        self.assertEqual(self.db.get_top_n_modified(3), ["A(1)", "B(1)", "C(1)"])

    def test_deleting_last_field_drops_key_from_ranking(self):
        self.db.set("A", "x", 1)
        self.db.set("B", "x", 1)
        self.db.delete("A", "x")  # removes A's only field -> record gone
        self.assertEqual(self.db.get_top_n_modified(5), ["B(1)"])

    def test_deleting_one_of_several_fields_still_counts(self):
        self.db.set("A", "x", 1)
        self.db.set("A", "y", 1)
        self.db.delete("A", "x")  # A still has field y -> still tracked
        self.assertEqual(self.db.get_top_n_modified(5), ["A(3)"])

    def test_n_larger_than_available_records(self):
        self.db.set("A", "x", 1)
        self.assertEqual(self.db.get_top_n_modified(10), ["A(1)"])


class TestLevel3(unittest.TestCase):
    def setUp(self):
        self.db = InMemoryDBLevel3()
        self.db.set("A", "count", 1)

    def test_lock_and_unlock_happy_path(self):
        self.assertTrue(self.db.lock("A", "c1"))
        self.assertTrue(self.db.unlock("A", "c1"))

    def test_lock_nonexistent_key_fails(self):
        self.assertFalse(self.db.lock("missing", "c1"))

    def test_double_lock_fails(self):
        self.assertTrue(self.db.lock("A", "c1"))
        self.assertFalse(self.db.lock("A", "c2"))

    def test_unlock_by_wrong_caller_fails(self):
        self.db.lock("A", "c1")
        self.assertFalse(self.db.unlock("A", "c2"))
        self.assertTrue(self.db.unlock("A", "c1"))

    def test_set_by_caller_blocked_by_other_lock(self):
        self.db.lock("A", "c1")
        self.assertFalse(self.db.set_by_caller("A", "count", 5, "c2"))
        self.assertEqual(self.db.get("A", "count"), 1)

    def test_set_by_caller_allowed_for_owner(self):
        self.db.lock("A", "c1")
        self.assertTrue(self.db.set_by_caller("A", "count", 5, "c1"))
        self.assertEqual(self.db.get("A", "count"), 6)

    def test_set_by_caller_allowed_when_unlocked(self):
        self.assertTrue(self.db.set_by_caller("A", "count", 5, "anyone"))
        self.assertEqual(self.db.get("A", "count"), 6)

    def test_delete_by_caller_blocked_by_other_lock(self):
        self.db.lock("A", "c1")
        self.assertFalse(self.db.delete_by_caller("A", "count", "c2"))

    def test_delete_by_caller_allowed_for_owner(self):
        self.db.lock("A", "c1")
        self.assertTrue(self.db.delete_by_caller("A", "count", "c1"))
        self.assertIsNone(self.db.get("A", "count"))


class TestLevel4(unittest.TestCase):
    def setUp(self):
        self.db = InMemoryDBLevel4()
        self.db.set("A", "count", 1)
        self.db.set("A", "name", 10)

    def test_undo_restores_pre_lock_state(self):
        self.db.lock("A", "c1")
        self.db.set_by_caller("A", "count", 100, "c1")
        self.db.delete_by_caller("A", "name", "c1")

        self.assertTrue(self.db.undo("A", "c1"))
        self.assertEqual(self.db.get("A", "count"), 1)
        self.assertEqual(self.db.get("A", "name"), 10)

    def test_undo_without_lock_fails(self):
        self.assertFalse(self.db.undo("A", "c1"))

    def test_undo_by_non_owner_fails(self):
        self.db.lock("A", "c1")
        self.assertFalse(self.db.undo("A", "c2"))

    def test_undo_is_idempotent(self):
        self.db.lock("A", "c1")
        self.db.set_by_caller("A", "count", 100, "c1")
        self.db.undo("A", "c1")
        self.assertTrue(self.db.undo("A", "c1"))
        self.assertEqual(self.db.get("A", "count"), 1)

    def test_logout_releases_all_locks_for_caller(self):
        self.db.set("B", "count", 1)
        self.db.lock("A", "c1")
        self.db.lock("B", "c1")

        self.assertEqual(self.db.logout("c1"), 2)
        self.assertFalse(self.db.unlock("A", "c1"))
        self.assertFalse(self.db.unlock("B", "c1"))
        # Locks released -> anyone can write again.
        self.assertTrue(self.db.set_by_caller("A", "count", 1, "c2"))

    def test_logout_only_affects_given_caller(self):
        self.db.set("B", "count", 1)
        self.db.lock("A", "c1")
        self.db.lock("B", "c2")

        self.assertEqual(self.db.logout("c1"), 1)
        self.assertFalse(self.db.set_by_caller("B", "count", 1, "c1"))  # B still locked by c2


if __name__ == "__main__":
    unittest.main()
