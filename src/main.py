from src.db.connect import _connect_to_db
from timedecorator import record_time
from user import get_user_move, get_difficulty
from sudoku_board import SudokuBoard, generate_new_board
from db.utils import get_board_from_db
from copy import deepcopy


# needs updating in user.py
def get_user_move():
    user_row = input(" Please select row (1-9): ")
    if user_row == 'exit':
        return 'exit'
    elif user_row == 'restart':
        return 'restart'
    else:
        user_row = int(user_row)
    user_col = int(input(" Please select column (1-9): "))
    if user_col == 'exit':
        return 'exit'
    elif user_col == 'restart':
        return 'restart'
    else:
        user_col = int(user_col)
    user_num = int(input(" Please enter number (1-9): "))
    if user_num == 'exit':
        return 'exit'
    elif user_num == 'restart':
        return 'restart'
    else:
        user_num = int(user_num)

    while not valid_number(user_row):
        user_row = int(input(" Invalid choice of row, please try again: "))
    while not valid_number(user_col):
        user_col = int(input(" Invalid choice of column, please try again: "))
    while not valid_number(user_num):
        user_num = int(input(" Invalid choice of number, please try again: "))

    return user_row - 1, user_col - 1, user_num


@record_time
def play_game(board):
    print("Type exit to return to menu at any point.")
    print("Type restart to clear the board.")
    restart_board = deepcopy(board)

    solved = False
    completed = board.check_completed()
    if completed:
        solved = board.check_solution()

    while not solved:
        print(board.format_board())
        user_move = get_user_move()
        if user_move == 'exit':
            # SAVE BOARD TO DATABASE
            board.save_board()
            print("Your game has been saved.")
            break
        elif user_move == 'restart':
            play_game(restart_board)
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

def main():
    print("Welcome to sudoku!")
    wants_to_play = True
    while wants_to_play:
        print_menu_options()
        choice = int(input("Please choose a menu option by typing it's number: "))
        if choice == 1:
            new_board = generate_new_board(get_difficulty())
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


if __name__ == "__main__":
    main()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# functions to create

# def store highscore/times/game history # database

# def get_time_taken

# def check_saved
