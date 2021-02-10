import unittest
from main import sum_two_numbers


class TestStringMethods(unittest.TestCase):

    def test_sum_two_numbers(self):
        cases = (
            (2, 3, 5),
            (3, 4, 7),
        )
        for arg1, arg2, expected in cases:
            with self.subTest(f"{arg1} + {arg2} = {expected}"):
                self.assertEqual(sum_two_numbers(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()
