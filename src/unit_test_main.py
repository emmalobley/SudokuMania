import unittest
from main import SudokuBoard

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


class MyTestCase(unittest.TestCase):

    def test_check_completed_on_incomplete(self):
        self.assertEqual(uncompletedBoard.check_completed(), False)

    def test_check_completed_on_complete(self):
        self.assertEqual(completed_correctBoard.check_completed(), True)

    def test_check_solution_on_correct(self):
        self.assertTrue(completed_correctBoard.check_solution())

    def test_check_solution_on_incorrect(self):
        self.assertFalse(completed_incorrectBoard.check_solution())


if __name__ == '__main__':
    unittest.main()
