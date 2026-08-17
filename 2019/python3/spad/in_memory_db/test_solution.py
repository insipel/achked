import unittest

from solution import InMemoryDB, process_queries


class TestInMemoryDBLevel1(unittest.TestCase):
    def test_set_returns_empty_string(self):
        db = InMemoryDB()
        self.assertEqual(db.set("A", "B", "E"), "")

    def test_get_existing_field(self):
        db = InMemoryDB()
        db.set("A", "B", "E")
        self.assertEqual(db.get("A", "B"), "E")

    def test_get_missing_record_or_field_returns_empty(self):
        db = InMemoryDB()
        self.assertEqual(db.get("A", "B"), "")
        db.set("A", "B", "E")
        self.assertEqual(db.get("A", "C"), "")
        self.assertEqual(db.get("X", "Y"), "")

    def test_set_overwrites_existing_field(self):
        db = InMemoryDB()
        db.set("A", "B", "E")
        db.set("A", "B", "G")
        self.assertEqual(db.get("A", "B"), "G")

    def test_delete_existing_field(self):
        db = InMemoryDB()
        db.set("A", "B", "E")
        self.assertEqual(db.delete("A", "B"), "true")
        self.assertEqual(db.get("A", "B"), "")

    def test_delete_missing_field_or_key(self):
        db = InMemoryDB()
        self.assertEqual(db.delete("A", "B"), "false")
        db.set("A", "B", "E")
        db.delete("A", "B")
        self.assertEqual(db.delete("A", "B"), "false")

    def test_process_queries_end_to_end(self):
        queries = [
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
        expected = ["", "E", "", "", "", "G", "true", "false", "", ""]
        self.assertEqual(process_queries(queries), expected)


if __name__ == "__main__":
    unittest.main()
