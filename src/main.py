from timedecorator import record_time
from user import get_user_move, get_difficulty, get_player_name
from sudoku_board import SudokuBoard, generate_new_board, format_db_board
from db.utils import get_unfinished_board, save_player, get_player_id
from copy import deepcopy


# function to play the game, wrapper records time before and after game is played and calcs time taken
@record_time
def play_game(board, player_id):
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
            board.save_board(player_id)  # needs player_id to save board
            # save board should also take timestamp as arg - store to db needs updating
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
        board.save_board(player_id)  # takes player_id as arg - should also take timestamp


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
    name = get_player_name()
    save_player(name)
    player_id = get_player_id(name)
    wants_to_play = True
    while wants_to_play:
        print_menu_options()
        choice = int(input("Please choose a menu option by typing it's number: "))
        if choice == 1:
            new_board = generate_new_board(get_difficulty())
            # timer decorator returns time as string (hh:mm:ss)
            time = play_game(new_board, player_id)
            print(time)
        if choice == 2:
            print("Here is your previously saved game: ")
            (old_time, continue_board) = format_db_board(get_unfinished_board(name))
            new_time = play_game(continue_board, player_id)
            print(new_time)
            # need function to add the two timestamps - store total

        if choice == 3:
            #     find highscores in database and print them here
            print("This is where highscores will go.")
        if choice == 4:
            print("Thank you for playing!")
            exit()


if __name__ == "__main__":
    main()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# functions to create

# def store highscore/times/game history # database

# def check_saved
