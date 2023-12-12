from src.db.utils import get_board_from_db
import requests


class SudokuBoard:
    def __init__(self, board, difficulty):
        self.board = board
        self.difficulty = difficulty

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

    # def get_board(self):
    #     return self.board

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


# boolean function, validate if sudoku is completed
# def completed_sudoku(board):
#     return


# get difficulty from user
def get_difficulty():
    difficulty = input("Please select difficulty: ").lower()
    while not valid_difficulty(difficulty):
        difficulty = input("Invalid choice. Please select difficulty: ").lower()
    return difficulty


# check user choice of number valid
def valid_difficulty(difficulty):
    return difficulty in {"easy", "medium", "hard"}


def get_sudoku_from_api(difficulty):
    endpoint = 'https://sudoku-game-and-api.netlify.app/api/sudoku'
    response = requests.get(endpoint)
    sudoku = response.json()
    return sudoku[difficulty]


def get_user_move():
    user_row = input(" Please select row (1-9): ")
    if user_row == 'exit':
        return 'exit'
    else:
        user_row = int(user_row)
    user_col = int(input(" Please select column (1-9): "))
    if user_col == 'exit':
        return 'exit'
    else:
        user_col = int(user_col)
    user_num = int(input(" Please enter number (1-9): "))
    if user_num == 'exit':
        return 'exit'
    else:
        user_num = int(user_num)

    while not valid_number(user_row):
        user_row = int(input(" Invalid choice of row, please try again: "))
    while not valid_number(user_col):
        user_col = int(input(" Invalid choice of column, please try again: "))
    while not valid_number(user_num):
        user_num = int(input(" Invalid choice of number, please try again: "))

    return user_row - 1, user_col - 1, user_num


# check user choice of number valid
def valid_number(number):
    return number in {1, 2, 3, 4, 5, 6, 7, 8, 9}


def generate_new_board():
    difficulty = get_difficulty()
    board = get_sudoku_from_api(difficulty)
    new_board = SudokuBoard(board, difficulty)
    print(f'    Difficulty = {difficulty.title()}')
    return new_board


def play_game(board):
    print("Type exit to return to menu at any point.")

    solved = False

    while not solved:
        print(board.format_board())
        user_move = get_user_move()
        if user_move == 'exit':
            # SAVE BOARD TO DATABASE
            print("Your game has been saved.")
            break
        board.update_board(user_move[0], user_move[1], user_move[2])
        completed = board.check_completed()
        if completed:
            solved = board.check_solution()
            if not solved:
                print("You've made a mistake somewhere.")
    # STOP TIMER
    # SAVE TIME, DIFFICULTY AND BOARD TO DATABASE
    if solved:
        print("Well done!")


# This is a test board to test the continue game option.
# Can be removed when connection to database is added.
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


menu_options = {1: "New Game",
                2: "Continue",
                3: "View Highscores",
                4: "Exit"}


def print_menu_options():
    for i in range(4):
        print(str(i + 1) + ": " + menu_options[i + 1])


# ~~~~~~~~~~~ main game loop ~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
    print("Welcome to sudoku!")
    wants_to_play = True
    while wants_to_play:
        print_menu_options()
        choice = int(input("Please choose a menu option by typing it's number: "))
        if choice == 1:
            new_board = generate_new_board()
            play_game(new_board)
        if choice == 2:
            print("Here is your previously saved game: ")
            print(get_board_from_db())
            #     fetch most recent board from database here
            test_board = uncompletedBoard
            play_game(test_board)
        if choice == 3:
            #     find highscores in database and print them here
            print("This is where highscores will go.")
        if choice == 4:
            print("Thank you for playing!")
            wants_to_play = False
            exit()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# functions to create

# def store highscore/times/game history # database

# def get_time_taken

# def check_saved

# def restart_puzzle
