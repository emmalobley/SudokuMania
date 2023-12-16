from timedecorator import record_time, convert_secs_to_hhmmss, convert_hhmmss_to_seconds
from user import get_user_move, get_difficulty, get_player_name, get_user_score
from sudoku_board import SudokuBoard, generate_new_board, format_db_board
from db.utils import get_unfinished_board, save_player, get_player_id
from copy import deepcopy


# play_game takes board, player_id and previous_time as inputs
# board is an object in the sudoku class
# player_id is the id of the player logged in (integer)
# previous_time is the recorded time in seconds for the previously saved game if the user is continuing a game, else
# it is set 0 if the user is starting a new game
def play_game(board, player_id, previous_time):

    restart_board = deepcopy(board)
    total_time = previous_time
    while True:
        # run the sudoku game loop, this breaks either when the game is solved or if the user types pause
        time_taken_seconds = sudoku_game_loop(board)
        total_time += time_taken_seconds
        formatted_time = convert_secs_to_hhmmss(total_time)

        if board.check_completed():
            solved = board.check_solution()
            if solved:
                print("Well done!")
                board.save_board(player_id, formatted_time)
                print(f"Time taken to solve sudoku (hh:mm:ss): {formatted_time}")
                return
            else:
                print("You have made a mistake somewhere.")
        else:
            print("Type exit to save your game and exit to the main menu.")
            print("Type restart to restart the game.")
            print("Type continue to continue playing the game.")
            choice = input("")
            if choice == 'exit':
                board.save_board(player_id, formatted_time)
                print(f"Time taken so far (hh:mm:ss): {formatted_time}")
                return
            elif choice == 'restart':
                board = deepcopy(restart_board)


@record_time
def sudoku_game_loop(board):
    print("Type pause to pause the timer and access exit, restart and continue functions.")
    solved = False
    while not solved:
        print(board.format_board())
        user_move = get_user_move()

        if user_move == 'pause':
            print("Timer paused.")
            break

        board.update_board(user_move[0], user_move[1], user_move[2])
        completed = board.check_completed()
        if completed:
            solved = board.check_solution()
            if not solved:
                print("You've made a mistake somewhere.")


def print_menu_options():
    menu_options = {1: "New Game",
                    2: "Continue",
                    3: "View Highscores",
                    4: "Exit"}
    for i in range(4):
        print(str(i + 1) + ": " + menu_options[i + 1])


# get choice from user - handles exception
def get_choice():
    while True:
        try:
            choice = int(input("Please choose a menu option by typing it's number: "))
            while choice not in [1, 2, 3, 4]:
                choice = int(input("Invalid, try again."))

            break
        except ValueError:
            print("Invalid, try again.")
    return choice


# ~~~~~~~~~~~ main game loop ~~~~~~~~~~~~~~~~~~

def main():
    print("Welcome to sudoku!")
    name = get_player_name()
    save_player(name)
    player_id = get_player_id(name)
    wants_to_play = True
    while wants_to_play:
        print_menu_options()
        choice = get_choice()
        if choice == 1:
            new_board = generate_new_board(get_difficulty())
            play_game(new_board, player_id, 0)

        if choice == 2:
            try:
                (previous_time, continue_board) = format_db_board(get_unfinished_board(name))
                print("Here is your previously saved game: ")
                print(f"Time taken so far (hh:mm:ss): {convert_secs_to_hhmmss(previous_time)}")
                play_game(continue_board, player_id, previous_time)
            except TypeError:
                print("No unfinished puzzles for this user")

        if choice == 3:
            get_user_score(name)

        if choice == 4:
            print("Thank you for playing!")
            exit()


if __name__ == "__main__":
    main()
