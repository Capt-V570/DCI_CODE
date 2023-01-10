import unittest
from math_operations import sub


class TestSubtraction(unittest.TestCase):
    def test_sub(self):
        self.assertEqual(sub(2, 2), 0)


if __name__ == "__main__":
    unittest.main()
