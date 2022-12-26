import unittest
import time

from metric_classes import Stats


class TestStats(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.singleton = Stats()

    def test_is_singleton(self):
        stat = Stats()
        stat2 = Stats()
        stat3 = Stats()
        self.assertEqual(id(self.singleton), id(stat))
        self.assertEqual(id(stat), id(stat2))
        self.assertEqual(id(stat2), id(stat3))
        self.assertEqual(id(stat), id(stat3))
        self.assertEqual(id(self.singleton), id(stat3))

    def test_time_stats(self):
        def __sleeper(time_sleep):
            time.sleep(time_sleep)

        with self.singleton.timer("sleeper"):
            __sleeper(0.5)

        time_stats = self.singleton.collect()["sleeper.timer"]
        self.assertAlmostEqual(time_stats, 0.5, delta=0.01)

        with self.assertRaises(KeyError):
            _ = self.singleton.collect()["sleeper.timer"]

        with self.singleton.timer("sleeper"):
            __sleeper(0.5)
            __sleeper(0.5)

        time_stats = self.singleton.collect()["sleeper.timer"]
        self.assertAlmostEqual(time_stats, 1, delta=0.02)
        with self.assertRaises(KeyError):
            _ = self.singleton.collect()["sleeper.timer"]

        start_time = time.time()
        __sleeper(0.5)
        self.singleton.timer("sleeper").add(time.time() - start_time)
        time_stats = self.singleton.collect()["sleeper.timer"]
        self.assertAlmostEqual(time_stats, 0.5, delta=0.02)
        with self.assertRaises(KeyError):
            _ = self.singleton.collect()["sleeper.timer"]

        start_time = time.time()
        __sleeper(0.5)
        self.singleton.timer("sleeper").add(time.time() - start_time)
        self.singleton.timer("sleeper").add(time.time() - start_time)
        time_stats = self.singleton.collect()["sleeper.timer"]
        self.assertAlmostEqual(time_stats, 1, delta=0.02)
        with self.assertRaises(KeyError):
            _ = self.singleton.collect()["sleeper.timer"]

    def test_counter_stat(self):
        self.singleton.count("foo").add()
        self.assertEqual(self.singleton.collect()["foo.count"], 1)
        with self.assertRaises(KeyError):
            _ = self.singleton.collect()["foo.count"]

        self.singleton.count("foo").add()
        self.singleton.count("foo").add()
        self.singleton.count("foo").add()
        self.singleton.count("foo").add()
        self.singleton.count("foo").add()
        self.assertEqual(self.singleton.collect()["foo.count"], 5)
        with self.assertRaises(KeyError):
            _ = self.singleton.collect()["foo.count"]

    def test_avg_stat(self):
        self.singleton.avg("foo").add(1)
        self.assertEqual(self.singleton.collect()["foo.avg"], 1)

        self.singleton.avg("foo").add(1)
        self.singleton.avg("foo").add(2)
        self.singleton.avg("foo").add(3)
        self.assertEqual(self.singleton.collect()["foo.avg"], 2)

        with self.assertRaises(KeyError):
            _ = self.singleton.collect()["foo.avg"]


if __name__ == '__main__':
    unittest.main()
