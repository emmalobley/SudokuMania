from timedecorator import record_time
from user import get_user_move, get_difficulty
from sudoku_board import SudokuBoard, generate_new_board
from db.utils import get_unfinished_boards, save_player
from copy import deepcopy


# function to play the game, wrapper records time before and after game is played and calcs time taken
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
            board.save_board('1')  # needs player_id as additional argument for now
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
        board.save_board('1')  # needs player_id as additional argument for now


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

# could this be within the print_menu_opt function?
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
    save_player("Jane")
    wants_to_play = True
    while wants_to_play:
        print_menu_options()
        choice = int(input("Please choose a menu option by typing it's number: "))
        if choice == 1:
            new_board = generate_new_board(get_difficulty())
            play_game(new_board)
        if choice == 2:
            print("Here is your previously saved game: ")
            print(get_unfinished_boards("Jane"))  # name placeholder
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

# def check_saved
