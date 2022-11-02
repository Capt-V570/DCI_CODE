import unittest
from string_operations import join_names


class TestJoinNames(unittest.TestCase):
    def test_join_names(self):
        self.assertEqual(join_names(['Fausto', 'Victor']), 'FaustoVictor')


if __name__ == "__main__":
    unittest.main()