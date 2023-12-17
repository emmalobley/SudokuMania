import unittest

from src.user import valid_number, valid_difficulty


class UserTests(unittest.TestCase):

    # test valid_number and valid_difficulty
    def test_valid_numbers(self):
        with self.assertRaises(Exception):
            valid_number()

        self.assertTrue(valid_number(1))
        self.assertFalse(valid_number(11))
        self.assertFalse(valid_number("1"))

    def test_valid_difficulty(self):
        with self.assertRaises(Exception):
            valid_difficulty()
        self.assertTrue("easy")
        self.assertTrue("Medium")
        self.assertFalse(0)


if __name__ == '__main__':
    unittest.main()
