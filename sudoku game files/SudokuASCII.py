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

def completedsudoku(board, solution):
    return board == solution

# loop until you get a board of your chosen difficulty ~ .title so input won't be case sens
def get_sudoku(difficulty =input("pick your difficulty: ").title()):
    while True:
        endpoint = "https://sudoku-api.vercel.app/api/dosuku"
        response = requests.get(endpoint)
        sudoku = response.json()['newboard']['grids'][0]

        if sudoku['difficulty'] == difficulty:
            return sudoku['value'], sudoku['solution'], sudoku['difficulty']

# ~~~~~~~~~~~ main game loop ~~~~~~~~~~~~~~~~~~

def main():
    board, solution, difficulty = get_sudoku()
    print("     Welcome to sudoku! ")
    print(f'    Difficulty = {difficulty}')
    # pp(board)

    while not completedsudoku(board, solution):

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

        user_row = int(input(" Please select row (1-9): "))
        user_col = int(input(" Please select col (1-9): "))
        user_num = int(input(" Please enter number (1-9): "))

        # zero-indexing :(
        user_row -= 1
        user_col -= 1


        if solution[user_row][user_col] == user_num:
            print("         Correct!")
            board[user_row][user_col] = user_num

        else:
            print(" Incorrect. Try again.")


        # pp(board)


if __name__ == "__main__":
    main()
