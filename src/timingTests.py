import unittest

from src.timedecorator import record_time, convert_secs_to_hhmmss, convert_hhmmss_to_seconds
import time


# functions below to simulate the game getting timed for testing
@record_time
def mock_game():
    time.sleep(6)  # insert time in seconds here to test


class TimingTestCases(unittest.TestCase):

    # testing functions from timedecorator.py
    def test_record_time_decorator_6secs(self):
        self.assertTrue(mock_game, 6)

    def test_convert_hhmmss_to_secs_1hour(self):
        self.assertEqual(convert_hhmmss_to_seconds("01:00:00"), 3600)

    def test_convert_hhmmss_to_secs_0hours(self):
        self.assertEqual(convert_hhmmss_to_seconds("00:00:00"), 0)

    def test_convert_hhmmss_to_secs_100hours(self):
        self.assertEqual(convert_hhmmss_to_seconds("100:00:00"), 360000)

    def test_convert_secs_to_hhmmss_0secs(self):
        self.assertEqual("00:00:00", convert_secs_to_hhmmss(0))

    def test_convert_secs_to_hhmmss_60secs(self):
        self.assertEqual("00:01:00", convert_secs_to_hhmmss(60))


if __name__ == '__main__':
    unittest.main()
