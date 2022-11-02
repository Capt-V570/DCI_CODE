import unittest
from math_operations import multiplication


class TestMultiplication(unittest.TestCase):
    def test_multiplications(self):
        self.assertEqual(multiplication(2, 2), 4)


if __name__ == "__main__":
    unittest.main()
