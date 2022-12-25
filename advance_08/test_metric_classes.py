import unittest
from time import time, sleep

from metric_classes import Stats


class StatsTest(unittest.TestCase):
    def test_time_module(self):
        def wait_func(delay):
            sleep(delay)

        with Stats.timer("calc"):  # 0.2
            wait_func(0.2)

        res_time = Stats.collect()['calc.timer']
        self.assertAlmostEqual(res_time, 0.2, delta=0.01)
        self.assertDictEqual(Stats.collect(), {})

        with Stats.timer("calc"):  # 0.5
            wait_func(0.2)
            wait_func(0.3)

        res_time = Stats.collect()['calc.timer']
        self.assertAlmostEqual(res_time, 0.5, delta=0.01)
        self.assertDictEqual(Stats.collect(), {})

        t1 = time()
        wait_func(0.7)  # 7
        t2 = time()
        Stats.timer("calc").add(t2 - t1)  # 0.7

        res_time = Stats.collect()['calc.timer']
        self.assertAlmostEqual(res_time, 0.7, delta=0.01)
        self.assertDictEqual(Stats.collect(), {})

        t1 = time()
        wait_func(0.5)  # 7
        t2 = time()
        Stats.timer("calc").add(t2 - t1)  # 0.5
        Stats.timer("calc").add(t2 - t1)  # 1

        res_time = Stats.collect()['calc.timer']
        self.assertAlmostEqual(res_time, 1, delta=0.01)
        self.assertDictEqual(Stats.collect(), {})

    def test_avg_module(self):
        Stats.avg("calc").add(1)
        res_avg = Stats.collect()['calc.avg']
        self.assertEqual(res_avg, 1)

        Stats.avg("calc").add(1)
        Stats.avg("calc").add(9)
        Stats.avg("calc").add(4)
        Stats.avg("calc").add(6)
        res_avg = Stats.collect()['calc.avg']
        self.assertEqual(res_avg, 5)

        self.assertDictEqual(Stats.collect(), {})

    def test_count_module(self):
        Stats.count("calc").add()
        res_avg = Stats.collect()['calc.count']
        self.assertEqual(res_avg, 1)

        Stats.count("calc").add()
        Stats.count("calc").add()
        Stats.count("calc").add()
        Stats.count("calc").add()
        res_avg = Stats.collect()['calc.count']
        self.assertEqual(res_avg, 4)

        self.assertDictEqual(Stats.collect(), {})

    def test_empty(self):
        Stats.count("calc")
        Stats.count("empty")
        self.assertDictEqual(Stats.collect(), {})


if __name__ == '__main__':
    unittest.main()
