import unittest
from lru_cache import LRUCache


class LRUTests(unittest.TestCase):

    def test_set(self):
        lru = LRUCache(2)
        self.assertEqual(lru.data_dict, {})
        lru.set(1, 1)
        self.assertEqual(lru.data_dict, {1: 1})
        lru.set(2, 2)
        self.assertEqual(lru.data_dict, {1: 1, 2: 2})
        lru.set(3, 3)
        self.assertEqual(lru.data_dict, {3: 3, 2: 2})
        
    def test_get(self):
        lru = LRUCache(2)
        self.assertEqual(lru.get(0), -1)
        lru.set(1, 1)
        lru.set(2, 2)
        self.assertEqual(lru.get(1), 1)
        self.assertEqual(lru.get(2), 2)

    def test_replace_cases(self):
        lru = LRUCache(2)
        self.assertEqual(lru.data_dict, {})
        lru.set(1, 1)
        self.assertEqual(lru.data_dict, {1: 1})
        lru.set(2, 2)
        self.assertEqual(lru.data_dict, {1: 1, 2: 2})
        self.assertEqual(lru.get(1), 1)
        lru.set(5, 5)
        self.assertEqual(lru.data_dict, {1: 1, 5: 5})
        lru.set(6, 6)
        self.assertEqual(lru.get(5), 5)
        lru.set(7, 7)
        self.assertEqual(lru.get(5), 5)
        lru.set(9, 9)
        self.assertEqual(lru.data_dict, {5: 5, 9: 9})


if __name__ == '__main__':
    unittest.main()
