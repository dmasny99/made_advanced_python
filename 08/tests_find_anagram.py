from find_anagram import find_anagrams
import unittest

class TestFinder(unittest.TestCase):

    def test_finder(self):
        pattern = 'a'
        text = 'aaaaaa'
        self.assertEqual(find_anagrams(text, pattern), [0, 1, 2, 3, 4, 5])

        pattern = 'ab'
        text = 'abab'
        self.assertEqual(find_anagrams(text, pattern), [0, 1, 2])

        pattern = ''
        text = 'abab'
        self.assertEqual(find_anagrams(text, pattern), [])

        pattern = 'с'
        text = 'abab'
        self.assertEqual(find_anagrams(text, pattern), [])

        pattern = 'abccccc'
        text = 'abab'
        self.assertEqual(find_anagrams(text, pattern), [])

        pattern = 'ab'
        text = 'abcbdecbdeafsfggefgsbc'
        self.assertEqual(find_anagrams(text, pattern), [0])

        pattern = 'bd'
        text = 'abcbdecbdeafsfggefgsbc'
        self.assertEqual(find_anagrams(text, pattern), [3, 7])

        pattern = 'fc'
        text = 'fcffccffcccfccf'
        self.assertEqual(find_anagrams(text, pattern), [0, 1, 3, 5, 7, 10, 11, 13])



if __name__ == '__main__':
    unittest.main()