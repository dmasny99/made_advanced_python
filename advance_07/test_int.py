import unittest


class TestInt(unittest.TestCase):

    def test_convert_float_to_int(self):
        floats = [0.1, 0.2, 0.55, 1.0, 0.99, 1.17, 1]
        true_ints = [0, 0, 0, 1, 0, 1, 1]
        for idx, element in enumerate(floats):
            int_elem = int(element)
            self.assertIsInstance(int_elem, int)
            self.assertEqual(int_elem, true_ints[idx])

    def test_invalid_convert(self):

        def __convert_to_int(elem):
            return int(elem)

        invalid_data_value_error = ["", "abc"]
        invalid_data_type_error = [[1, 2, 3], {"abc": 123}]

        for elem in invalid_data_value_error:
            self.assertRaises(ValueError, __convert_to_int, elem)
        for elem in invalid_data_type_error:
            self.assertRaises(TypeError, __convert_to_int, elem)

    def test_convert_from_different_ns(self):
        numbers = {
            8: ["1000", "22", "10", "8", "8"],
            16: ["10000", "121", "20", "10", "G"],
            123: ["1111011", "11120", "173", "7B", "3F"],
            }
        number_systems = [2, 3, 8, 16, 36]
        for num in numbers.items():
            for idx, representation in enumerate(numbers[num[0]]):
                int_elem = int(representation, number_systems[idx])
                self.assertIsInstance(int_elem, int)
                self.assertEqual(int_elem, num[0])


if __name__ == "__main__":
    unittest.main()
