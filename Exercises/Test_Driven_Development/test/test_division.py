import unittest
from math_operations import division


class TestDivision(unittest.TestCase):
    def test_division(self):
        self.assertEqual(division(2, 2), 1)


if __name__ == "__main__":
    unittest.main()
