import unittest


class TestStrPartition(unittest.TestCase):

    def test_partition_output(self):
        string = "abc"
        result = string.partition(".")
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)

    def test_left_partition(self):
        strings = ["_abc", " abc", ".abc"]
        separators = ["_", " ", "."]
        for idx, elem in enumerate(strings):
            result = elem.partition(separators[idx])
            self.assertTupleEqual(result, ("", separators[idx], elem[1:]))

    def test_right_partition(self):
        strings = ["abc_", "abc ", "abc."]
        separators = ["_", " ", "."]
        for idx, elem in enumerate(strings):
            result = elem.partition(separators[idx])
            self.assertTupleEqual(result, (elem[:-1], separators[idx], ""))

    def test_left_right_partition(self):  # actually the same as left one
        strings = ["_abc_", " abc ", ".abc."]
        separators = ["_", " ", "."]
        for idx, elem in enumerate(strings):
            result = elem.partition(separators[idx])
            self.assertTupleEqual(result, ("", separators[idx], elem[1:]))

    def test_repeating_pattern_partition(self):
        strings = ["_abc_abc_", " abc abc ", ".abc.abc."]
        separators = ["_", " ", "."]
        for idx, elem in enumerate(strings):
            result = elem.partition(separators[idx])
            self.assertTupleEqual(result, ("", separators[idx], elem[1:]))

    def test_missing_separator_partition(self):
        string = "abcabc"
        separators = ["_", " ", "."]
        for sep in separators:
            result = string.partition(sep)
            self.assertTupleEqual(result, (string, "", ""))

    def test_multiple_separators_patririon(self):
        strings = [
            " .abc_./abc_",
            "_.a bc abc ",
            ".// __ abc..//__  ,,,abc.,,  .."
            ]
        separators = ["_", " ", "."]
        results = [
            (" .abc", separators[0], "./abc_"),
            ("_.a", separators[1], "bc abc "),
            ("", separators[2], "// __ abc..//__  ,,,abc.,,  .."),
            ]
        for idx, elem in enumerate(strings):
            result = elem.partition(separators[idx])
            self.assertTupleEqual(result, results[idx])

    def test_complex_separator_partition(self):
        strings = ["_abc_./abc_", " abc .,. abc ", "  .'kk'abc.abc."]
        separators = ["_./", ".,.", "'kk'"]
        results = [
            ("_abc", separators[0], "abc_"),
            (" abc ", separators[1], " abc "),
            ("  .", separators[2], "abc.abc."),
            ]
        for idx, elem in enumerate(strings):
            result = elem.partition(separators[idx])
            self.assertTupleEqual(result, results[idx])

    def test_whose_string_partition(self):
        strings = ["_abc_./abc_", " abc .,. abc ", "  .'kk'abc.abc."]
        separators = strings
        results = [
            ("", separators[0], ""),
            ("", separators[1], ""),
            ("", separators[2], ""),
            ]
        for idx, elem in enumerate(strings):
            result = elem.partition(separators[idx])
            self.assertTupleEqual(result, results[idx])


if __name__ == "__main__":
    unittest.main()
