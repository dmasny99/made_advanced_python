import io
from ReaderWriter import * # на паре говорили, что так лучше не делать, но и километровую строку писать тоже не хочется
import unittest
import json
class ReadwrWriterTest(unittest.TestCase):
    # проверка на запись json
    def test_json_write(self):
        buf = io.StringIO()
        self.assertEqual(buf.getvalue(), '')
        dump_data({'name' : 'Jane', 'age' : 23, 'occupation' : 'teacher'}, buf, JsonWriter())
        self.assertEqual(buf.getvalue(), json.dumps({'name' : 'Jane', 'age' : 23, 'occupation' : 'teacher'}))

    # проверка на чтение json
    def test_json_read(self):
        buf = io.StringIO()
        self.assertEqual(buf.getvalue(), '')
        dump_data({'name' : 'Jane', 'age' : 23, 'occupation' : 'teacher'}, buf, JsonWriter())
        self.assertEqual(read_data(buf.getvalue(), JsonReader()), {'name' : 'Jane', 'age' : 23, 'occupation' : 'teacher'})
    
    # проверка на запись txt
    def test_txt_write(self):
        buf = io.StringIO()
        self.assertEqual(buf.getvalue(), '')
        dump_data(['abc', 'sdfsf', 'sfsf'], buf, TxtWriter())
        self.assertEqual(buf.getvalue(), 'abc\nsdfsf\nsfsf')

        buf = io.StringIO()
        dump_data('abc', buf, TxtWriter())
        self.assertEqual(buf.getvalue(), 'abc')

    # проверка на чтение txt
    def test_txt_read(self):
        buf = io.StringIO()
        self.assertEqual(buf.getvalue(), '')
        dump_data(['abc', 'sdfsf', 'sfsf'], buf, TxtWriter())
        buf.seek(0)
        self.assertEqual(read_data(buf, TxtReader()), ['abc', 'sdfsf', 'sfsf'])

        buf = io.StringIO()
        self.assertEqual(buf.getvalue(), '')
        dump_data('abc', buf, TxtWriter())
        buf.seek(0)
        self.assertEqual(read_data(buf, TxtReader()), ['abc'])

    # проверка на запись csv
    def test_csv_write(self):
        buf = io.StringIO()
        self.assertEqual(buf.getvalue(), '')
        dump_data(['word1', 'word2', 'word3'], buf, CsvWriter())
        print(buf.getvalue())
        self.assertEqual(buf.getvalue(), 'word1,word2,word3\r\n')
    # проверка на чтение csv
    def test_csv_read(self):
        buf = io.StringIO()
        self.assertEqual(buf.getvalue(), '')
        dump_data(['word1', 'word2', 'word3'], buf, CsvWriter())
        buf.seek(0)
        self.assertEqual(read_data(buf, CsvReader()), ['word1,word2,word3'])

        dump_data(['word4', 'word5', 'word6'], buf, CsvWriter())
        buf.seek(0)
        self.assertEqual(read_data(buf, CsvReader()), ['word1,word2,word3', 'word4,word5,word6'])
        
if __name__ == '__main__':
    unittest.main()