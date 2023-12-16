import requests
from db.utils import save_board_to_db


# objects for this class are created for each board used by a player - new or continued
class SudokuBoard:
    def __init__(self, board, difficulty):
        self.board = board
        self.difficulty = difficulty

    # format board in ascii frame for better user readability
    def format_board(self):
        ascii_board = "\=======+=======+=======/\n" \
                      "| . . . | . . . | . . . |\n" \
                      "| . . . | . . . | . . . |\n" \
                      "| . . . | . . . | . . . |\n" \
                      "+-------+-------+-------+\n" \
                      "| . . . | . . . | . . . |\n" \
                      "| . . . | . . . | . . . |\n" \
                      "| . . . | . . . | . . . |\n" \
                      "+-------+-------+-------+\n" \
                      "| . . . | . . . | . . . |\n" \
                      "| . . . | . . . | . . . |\n" \
                      "| . . . | . . . | . . . |\n" \
                      "/=======+=======+=======\ "

        # store sudoku board as list
        single_list = [num for slist in self.board for num in slist]

        result = ""
        index = 0

        for char in ascii_board:
            if char == '.' and single_list[index] != 0:
                # put numbers into asciiBoard
                result += str(single_list[index])
                index += 1
            elif char == ".":
                # 0's in board stored as dot
                result += char
                index += 1
            else:
                result += char

        return result

    # update a given cell in board with new number
    def update_board(self, row, col, num):
        self.board[row][col] = num

    # This function checks whether the board is filled in
    def check_completed(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return False
        return True

    # This function will return True if the board is a valid solution
    def check_solution(self):
        # check there are unique numbers in each row
        for i in range(9):
            if len(set([x for x in self.board[i]])) != 9:
                return False
        # check there are unique numbers in each column
        for j in range(9):
            if len(set([self.board[i][j] for i in range(9)])) != 9:
                return False
        # check there are unique numbers in each square
        for i in range(3):
            for j in range(3):
                digits_in_square = [self.board[3 * i + a][3 * j] for a in range(3)] + [self.board[3 * i + a][3 * j + 1]
                                                                                       for a in range(3)] + [
                                       self.board[3 * i + a][3 * j + 2] for a in range(3)]

                if len(set(digits_in_square)) != 9:
                    return False
        return True

    # formats board as dictionary and uses dictionary to save board to db
    def save_board(self, player_id, time):
        boards_data = {
            "player_id": player_id,
            "difficulty": self.difficulty,
            "completed": int(self.check_completed()),  # need in form as int for sql
            "total_time": time
            }
        for i, line in enumerate(self.board):
            boards_data["row_{}".format(i + 1)] = ''.join(map(str, line))
        save_board_to_db(boards_data)


# call to api with difficulty choice
def get_sudoku_from_api(difficulty):
    endpoint = 'https://sudoku-game-and-api.netlify.app/api/sudoku'
    response = requests.get(endpoint)
    sudoku = response.json()
    return sudoku[difficulty]


# generates object of SudokuBoard class from board retrieved from API
def generate_new_board(difficulty):
    board = get_sudoku_from_api(difficulty)
    new_board = SudokuBoard(board, difficulty)
    print(f'    Difficulty = {difficulty.title()}')
    return new_board


# takes tuple with difficulty, time and 9 strings of 9 digits as arg and converts to correct format
# used when user continues board retrieved from db
def format_db_board(db_board):
    board = []
    difficulty = db_board[0]
    time = db_board[1]
    db_board = db_board[2:]
    for line in db_board:
        board.append(list(map(int, line)))
    return time, SudokuBoard(board, difficulty)
