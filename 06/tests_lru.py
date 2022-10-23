import unittest
from lru_cache import LRUCache


class LRUTests(unittest.TestCase):

    def test_set(self):
        lru = LRUCache(2)
        self.assertEqual(lru.data_dict, {})
        lru.set(1, 1)
        self.assertEqual(lru.get(1), 1)
        lru.set(2, 2)
        self.assertEqual(lru.get(1), 1)
        self.assertEqual(lru.get(2), 2)
        lru.set(3, 3)
        self.assertEqual(lru.get(2), 2)
        self.assertEqual(lru.get(3), 3)
        self.set(2,2)

    def test_from_task(self):
        lru = LRUCache(2)
        lru.set('k1', 'val1')
        lru.set('k2', 'val2')
        self.assertIsNone(lru.get('k3'))
        self.assertEqual(lru.get('k2'), 'val2')
        self.assertEqual(lru.get('k1'), 'val1')

        lru.set('k3', 'val3')
        print(lru.get('k3'))
        self.assertEqual(lru.get('k3'), 'val3')
        self.assertIsNone(lru.get('k2'))
        self.assertEqual(lru.get('k1'), 'val1')

    def test_capacity_one(self):
        lru = LRUCache(1)
        lru.set('k1', 'val1')
        self.assertEqual(lru.get('k1'), 'val1')
        lru.set('k2', 'val2')
        self.assertEqual(lru.get('k2'), 'val2')
        lru.set('k3', 'val3')
        lru.set('k4', 'val4')
        self.assertEqual(lru.get('k4'), 'val4')
        self.assertIsNone(lru.get('k3'))

    def test_full_replacement(self):
        lru = LRUCache(3)
        lru.set('k1', 'val1')
        lru.set('k2', 'val2')
        lru.set('k3', 'val3')

        self.assertEqual(lru.get('k1'), 'val1')
        self.assertEqual(lru.get('k2'), 'val2')
        self.assertEqual(lru.get('k3'), 'val3')

        lru.set('k4', 'val4')
        lru.set('k5', 'val5')
        lru.set('k6', 'val6')

        self.assertEqual(lru.get('k4'), 'val4')
        self.assertEqual(lru.get('k5'), 'val5')
        self.assertEqual(lru.get('k6'), 'val6')

        self.assertIsNone(lru.get('k1'))
        self.assertIsNone(lru.get('k2'))
        self.assertIsNone(lru.get('k3'))

    def test_rewrite_key(self):
        lru = LRUCache(3)
        lru.set('k1', 'val1')
        lru.set('k2', 'val2')
        lru.set('k3', 'val3')

        self.assertEqual(lru.get('k1'), 'val1')
        self.assertEqual(lru.get('k2'), 'val2')
        self.assertEqual(lru.get('k3'), 'val3')

        lru.set('k1', 'val1_new')
        self.assertEqual(lru.get('k1'), 'val1_new')

        lru.set('k4', 'val4')
        self.assertEqual(lru.get('k1'), 'val1_new')
        self.assertIsNone(lru.get('k2'))
        self.assertEqual(lru.get('k3'), 'val3')
        self.assertEqual(lru.get('k4'), 'val4')

        lru.set('k1', 'val1_new_new')
        self.assertEqual(lru.get('k1'), 'val1_new_new')

        lru.set('k5', 'val5')
        self.assertEqual(lru.get('k1'), 'val1_new_new')
        self.assertIsNone(lru.get('k3'))
        self.assertEqual(lru.get('k4'), 'val4')
        self.assertEqual(lru.get('k5'), 'val5')

if __name__ == '__main__':
    unittest.main()
