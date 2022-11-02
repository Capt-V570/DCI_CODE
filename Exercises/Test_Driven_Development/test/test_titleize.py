import unittest
from string_operations import titleize_names


class TestTitleize(unittest.TestCase):
    def test_titleize(self):
        self.assertEqual(titleize_names('fausto', 'victor'), ('Fausto', 'Victor'))


if __name__ == "__main__":
    unittest.main()
