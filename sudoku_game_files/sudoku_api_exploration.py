import requests
import pandas as pd
from pprint import pprint as pp

endpoint = "https://sudoku-api.vercel.app/api/dosuku"

response = requests.get(endpoint)
sudoku = response.json()['newboard']['grids'][0]
board = sudoku['value']
solution = sudoku['solution']
difficulty = sudoku['difficulty']

# creating pandas data frame - adding row and col labels
pandaBoard = pd.DataFrame(board, index=[f'R{i+1}' for i in range(9)], columns=[f'C{i+1}' for i in range(9)])

asciiBoard = "+-------+-------+-------+\n" \
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
             "+-------+-------+-------+"

asciiBoard2 = "\=======+=======+=======/\n" \
             "| . . . | . . . | . . . |\n" \
             "| . . . | . . . | . . . |\n" \
             "| . . . | . . . | . . . |\n" \
             "+=======+=======+=======+\n" \
             "| . . . | . . . | . . . |\n" \
             "| . . . | . . . | . . . |\n" \
             "| . . . | . . . | . . . |\n" \
             "+=======+=======+=======+\n" \
             "| . . . | . . . | . . . |\n" \
             "| . . . | . . . | . . . |\n" \
             "| . . . | . . . | . . . |\n" \
             "/=======+=======+=======\ "

# pp(sudoku)
print("\nThis is a randomly generated sudoku board from API: ")
pp(board)
print("\nSolution to board: ")
pp(solution)

# pygame or turtle ---

# pandas table - labels help with identifying row/col # potential for jupyter notebooks etc interactive-ness
print("\nSudoku board in pandas format table: ")
print(pandaBoard)

# ASCII symbol board - different designs - could enter sudoku board data in a for loop
print("\nASCII option 1: ")
print(asciiBoard)

print("\nASCII option 2: ")
print(asciiBoard2)

# print difficulty and board for new game
print(f"\nNew Game - Difficulty : {difficulty}\n")
pp(board)

user_row = int(input("\nPlease select row (1-9): "))
user_col = int(input("Please select col (1-9): "))
user_num = int(input("Please enter number (1-9): "))

# for zero indexing
user_row -= 1
user_col -= 1


# check answers
if solution[user_row][user_col] == user_num:
    print("Correct!")
    board[user_row][user_col] = user_num
else:
    print("Incorrect. Try again.")

pp(board)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# loops for game running

# def fetch new board
#
# def solved (board, solution)
#     return board == solution
#
# while not solved(board, solution)
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# functions to create

# def select_difficulty

# def store highscore/times/game history # database

# def main

# def get_time_taken

# def get_new_board

# def check_saved

# def update_board

# def check_solution

# def restart_puzzle


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# class board()
#     def get_new_board
#
#     def check_solution
#
#     def update_board
