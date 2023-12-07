import requests
# import pandas as pd
# from pprint import pprint as pp


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

    def get_board(self):
        return self.board

    def update_board(self, row, col, num):
        self.board[row][col] = num


# boolean function, validate if sudoku is completed
# update check method - cannot compare to solution grid with this api
# def completed_sudoku(board, solution):
#     return board == solution


# get difficulty from user
def get_difficulty():
    # .title so input won't be case sens
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
    user_row = int(input(" Please select row (1-9): "))
    user_col = int(input(" Please select column (1-9): "))
    user_num = int(input(" Please enter number (1-9): "))

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


# ~~~~~~~~~~~ main game loop ~~~~~~~~~~~~~~~~~~

def main():
    difficulty = get_difficulty()
    board = get_sudoku_from_api(difficulty)
    new_board = SudokuBoard(board, difficulty)

    print("     Welcome to sudoku! ")
    print(f'    Difficulty = {difficulty.title()}')
    # pp(board)

    # cannot check against sol board so using i as placeholder for now
    i = 0
    while i < 10:  # not completed_sudoku(board, solution):
        print(new_board.format_board())
        user_move = get_user_move()
        new_board.update_board(user_move[0], user_move[1], user_move[2])


if __name__ == "__main__":
    while True:
        try:
            print("Press 'control' + 'd' to quit at any point.")
            main()
        except EOFError:
            break
