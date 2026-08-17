import unittest

from solution import TimeMap


class TestTimeMap(unittest.TestCase):
    def test_leetcode_example_1(self):
        tm = TimeMap()
        tm.set("foo", "bar", 1)
        self.assertEqual(tm.get("foo", 1), "bar")
        self.assertEqual(tm.get("foo", 3), "bar")

    def test_leetcode_example_2(self):
        tm = TimeMap()
        tm.set("love", "high", 10)
        tm.set("love", "low", 20)
        self.assertEqual(tm.get("love", 5), "")
        self.assertEqual(tm.get("love", 10), "high")
        self.assertEqual(tm.get("love", 15), "high")
        self.assertEqual(tm.get("love", 20), "low")
        self.assertEqual(tm.get("love", 25), "low")

    def test_get_before_any_set_returns_empty(self):
        tm = TimeMap()
        self.assertEqual(tm.get("missing", 1), "")

    def test_get_exact_timestamp_match(self):
        tm = TimeMap()
        tm.set("k", "v1", 1)
        tm.set("k", "v2", 5)
        tm.set("k", "v3", 10)
        self.assertEqual(tm.get("k", 5), "v2")

    def test_get_between_timestamps_returns_most_recent_prior(self):
        tm = TimeMap()
        tm.set("k", "v1", 1)
        tm.set("k", "v2", 5)
        tm.set("k", "v3", 10)
        self.assertEqual(tm.get("k", 7), "v2")

    def test_get_after_last_timestamp_returns_latest(self):
        tm = TimeMap()
        tm.set("k", "v1", 1)
        tm.set("k", "v2", 5)
        self.assertEqual(tm.get("k", 1000), "v2")

    def test_different_keys_are_independent(self):
        tm = TimeMap()
        tm.set("a", "a1", 1)
        tm.set("b", "b1", 1)
        self.assertEqual(tm.get("a", 1), "a1")
        self.assertEqual(tm.get("b", 1), "b1")
        self.assertEqual(tm.get("a", 2), "a1")


if __name__ == "__main__":
    unittest.main()
