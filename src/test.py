from src.timedecorator import record_time
from timedecorator import record_time
from user import get_user_move, get_difficulty, get_player_name
from sudoku_board import SudokuBoard, generate_new_board, format_db_board
from db.utils import get_unfinished_board, save_player
from copy import deepcopy



player = 'Helena'
message = """
hello {}""".format(player)

# print(message)

@record_time
def add( a, b):
    return a + b

# print(add(10, 5))


########################################################################

# @record_time
# def play_game(board):
#     print("Type exit to return to menu at any point.")
#     print("Type restart to clear the board.")
#     restart_board = deepcopy(board)
#
#     solved = False
#     completed = board.check_completed()
#     if completed:
#         solved = board.check_solution()
#
#     while not solved:
#         print(board.format_board())
#         user_move = get_user_move()
#         if user_move == 'exit':
#             # SAVE BOARD TO DATABASE
#             board.save_board('1')  # needs player_id as additional argument for now (could be player_name?)
#             # save board should also take timestamp as arg - store to db needs updating
#             print("Your game has been saved.")
#             break
#         elif user_move == 'restart':
#             play_game(restart_board)
#             break
#         board.update_board(user_move[0], user_move[1], user_move[2])
#         completed = board.check_completed()
#         if completed:
#             solved = board.check_solution()
#             if not solved:
#                 print("You've made a mistake somewhere.")
#     # STOP TIMER
#     # SAVE TIME, DIFFICULTY AND BOARD TO DATABASE
#     if solved:
#         print("Well done!")
#         board.save_board('1')  # takes player_id (or name?) as arg - should also take timestamp

########################################################################

def play_game(board):

    restart_board = deepcopy(board)
    total_time = 0  # <-- THIS NEEDS TO FIND THE CURRENT TIME IF THE SUDOKU IS LISTED IN THE DATABASE
    while True:
        # run the sudoku game loop, this breaks either when the game is solved or if the user types pause
        time_taken_seconds = sudoku_game_loop(board)
        total_time += time_taken_seconds

        if board.check_completed():
            solved = board.check_solution()
            if solved:
                print("Well done!")
                board.save_board('1', total_time)
                return
            else:
                print("You have made a mistake somewhere.")
        else:
            print("Type exit to save your game an exit to the main menu.")
            print("Type restart to restart the game.")
            print("Type continue to continue playing the game.")
            choice = input("")
            if choice == 'exit':
                board.save_board('1', total_time)
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

almost_complete = [[0, 2, 3, 6, 7, 8, 9, 4, 5],
                     [5, 8, 4, 2, 3, 9, 7, 6, 1],
                     [9, 6, 7, 1, 4, 5, 3, 2, 8],
                     [3, 7, 2, 4, 6, 1, 5, 8, 9],
                     [6, 9, 1, 5, 8, 3, 2, 7, 4],
                     [4, 5, 8, 7, 9, 2, 6, 1, 3],
                     [8, 3, 6, 9, 2, 4, 1, 5, 7],
                     [2, 1, 9, 8, 5, 7, 4, 3, 6],
                     [7, 4, 5, 3, 1, 6, 8, 9, 2]]
almost_completeBoard = SudokuBoard(almost_complete, 'easy')

play_game(almost_completeBoard)
