import unittest

from src.timedecorator import record_time, convert_secs_to_hhmmss, convert_hhmmss_to_seconds
from sudoku_board import SudokuBoard
from user import valid_number, valid_difficulty
import time

# boards:
# uncompleted board
uncompleted = [[0, 2, 1, 0, 9, 0, 5, 0, 0],
               [5, 7, 9, 0, 8, 4, 0, 2, 0],
               [6, 8, 4, 3, 2, 5, 0, 7, 9],
               [1, 4, 2, 0, 0, 9, 0, 0, 0],
               [7, 9, 3, 5, 0, 8, 2, 4, 1],
               [0, 5, 6, 4, 1, 2, 9, 0, 7],
               [9, 6, 0, 2, 7, 0, 4, 5, 0],
               [4, 1, 0, 0, 5, 3, 6, 9, 2],
               [2, 0, 5, 9, 4, 0, 7, 0, 8]]
uncompletedBoard = SudokuBoard(uncompleted, 'easy')
# completed and correct
completed_correct = [[1, 2, 3, 6, 7, 8, 9, 4, 5],
                     [5, 8, 4, 2, 3, 9, 7, 6, 1],
                     [9, 6, 7, 1, 4, 5, 3, 2, 8],
                     [3, 7, 2, 4, 6, 1, 5, 8, 9],
                     [6, 9, 1, 5, 8, 3, 2, 7, 4],
                     [4, 5, 8, 7, 9, 2, 6, 1, 3],
                     [8, 3, 6, 9, 2, 4, 1, 5, 7],
                     [2, 1, 9, 8, 5, 7, 4, 3, 6],
                     [7, 4, 5, 3, 1, 6, 8, 9, 2]]
completed_correctBoard = SudokuBoard(completed_correct, 'easy')
# completed with error (have changed board[0][0] from 1 to 2)
completed_incorrect = [[2, 2, 3, 6, 7, 8, 9, 4, 5],
                       [5, 8, 4, 2, 3, 9, 7, 6, 1],
                       [9, 6, 7, 1, 4, 5, 3, 2, 8],
                       [3, 7, 2, 4, 6, 1, 5, 8, 9],
                       [6, 9, 1, 5, 8, 3, 2, 7, 4],
                       [4, 5, 8, 7, 9, 2, 6, 1, 3],
                       [8, 3, 6, 9, 2, 4, 1, 5, 7],
                       [2, 1, 9, 8, 5, 7, 4, 3, 6],
                       [7, 4, 5, 3, 1, 6, 8, 9, 2]]
completed_incorrectBoard = SudokuBoard(completed_incorrect, 'easy')

# functions below to simulate the game getting timed for testing
@record_time
def mock_game():
    time.sleep(6)  # insert time in seconds here to test


class TestCases(unittest.TestCase):

    # testing sudoku board method check_complete
    def test_check_completed_on_incomplete(self):
        self.assertFalse(uncompletedBoard.check_completed())

    def test_check_completed_on_complete(self):
        self.assertTrue(completed_correctBoard.check_completed())

    # testing sudoku board method check_solution
    def test_check_solution_on_correct(self):
        self.assertTrue(completed_correctBoard.check_solution())

    def test_check_solution_on_incorrect(self):
        self.assertFalse(completed_incorrectBoard.check_solution())

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

    def test_connection_to_db(self):
        pass

# test_board = ('Easy', '00:23:11', '915678234', '743219568', '800054790', '109542680', '600793045', '050086009', '301467800',
#          '580921470', '204805900')
# current = time, continue_board = format_db_board(test_board)


if __name__ == '__main__':
    unittest.main()
