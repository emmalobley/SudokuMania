import requests
import pandas as pd
from pprint import pprint as pp
# loop until you get a board of your chosen difficulty
def get_sudoku(difficulty ='Easy'):
    while True:
        endpoint = "https://sudoku-api.vercel.app/api/dosuku"
        response = requests.get(endpoint)
        sudoku = response.json()['newboard']['grids'][0]

        if sudoku['difficulty'] == difficulty:
            return sudoku['value'], sudoku['solution'], sudoku['difficulty']

def main(): # loop to run game - check numbers against solution and return board with updated numbers
    board, solution, difficulty = get_sudoku()
    print("This is a randomly generated sudoku board from API: ")
    pp(difficulty)
    pp(board)

    while True:

        user_row = int(input("Please select row (1-9): "))
        user_col = int(input("Please select col (1-9): "))
        user_num = int(input("Please enter number (1-9): "))

        # zero-indexing :(
        user_row -= 1
        user_col -= 1


        if solution[user_row][user_col] == user_num:
            print("Correct!")
            board[user_row][user_col] = user_num
            # pandaBoard = pd.DataFrame(board, index=[f'R{i + 1}' for i in range(9)],
            #                           columns=[f'C{i + 1}' for i in range(9)])
            # print(pandaBoard)
        else:
            print("Incorrect. Try again.")

        pp(board)


if __name__ == "__main__":
    main()



