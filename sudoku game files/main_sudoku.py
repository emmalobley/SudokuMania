import requests
# import pandas as pd
# from pprint import pprint as pp

asciiBoard = "\=======+=======+=======/\n" \
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

# loop until you get a board of your chosen difficulty
# look into more efficient way of doing this if time allows
def get_sudoku(difficulty):
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

    return (user_row, user_col, user_num)

# check user choice of number valid
def valid_number(number):
    return number in {1, 2, 3, 4, 5, 6, 7, 8, 9}

# ~~~~~~~~~~~ main game loop ~~~~~~~~~~~~~~~~~~

def main():
    difficulty = get_difficulty()
    board = get_sudoku(difficulty)
    print("     Welcome to sudoku! ")
    print(f'    Difficulty = {difficulty.title()}')
    # pp(board)

    # cannot check against sol board so using i as placeholder for now
    i = 0
    while i < 10: # not completed_sudoku(board, solution):

        single_list = [num for slist in board for num in slist]

        # put sudoku list into a condensed list
        result = []
        index = 0

        # check if the character in the board is a '.'
        for char in asciiBoard:
            if char == '.':
                # check if the number is 0 / replace with dot if so
                if single_list[index] == 0:
                    result.append('.')
                else: # put numbers into asciiBoard
                    result.append(str(single_list[index]))
                index += 1
            else:
                result.append(char)

        asciiB_string = ''.join(result)
        print(asciiB_string)

        user_move = get_user_move()
        user_row = user_move[0] - 1
        user_col = user_move[1] - 1
        user_num = user_move[2]

        board[user_row][user_col] = user_num

        # if solution[user_row][user_col] == user_num:
        #     print("         Correct!")
        #     board[user_row][user_col] = user_num
        #
        # else:
        #     print(" Incorrect. Try again.")

        # pp(board)

if __name__ == "__main__":
    while True:
        try:
            print("Press 'control' + 'd' to quit at any point.")
            main()
        except EOFError:
            break
