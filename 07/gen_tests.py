import io
import unittest
from generator import generator


class ReadwrWriterTest(unittest.TestCase):

    def test_find_lines(self):
        # находит только строки состоящие из одной буквы а
        buf = io.StringIO('a\nbb\nabcd\naaabbb\nab\na')
        gen = generator(buf, ['a'])
        self.assertEqual(next(gen), 'a')
        self.assertEqual(next(gen), 'a')
        # невосприимчив к регистру
        buf = io.StringIO('A\nbb\nabcd\naaabbb\nab\na')
        gen = generator(buf, ['a'])
        self.assertEqual(next(gen), 'A')
        self.assertEqual(next(gen), 'a')

        buf = io.StringIO('a\nbb\nabcd\naaabbb\nab\na')
        gen = generator(buf, ['grgrgrr'])
        with self.assertRaises(StopIteration):
            next(gen)

        buf = io.StringIO('')
        gen = generator(buf, ['grgrgrr'])
        with self.assertRaises(StopIteration):
            next(gen)


if __name__ == '__main__':
    unittest.main()
