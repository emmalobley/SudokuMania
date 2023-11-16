#This API is called 'Dosuku'
#It generates sudoku boards and solutions
#This API is free and does not require any authentication!

#You can retrieve sudoku from urls

#https://sudoku-api.vercel.app/api/dosuku

import requests
from pprint import pprint as pp

endpoint = 'https://sudoku-api.vercel.app/api/dosuku'

response = requests.get(endpoint)
sudoku = response.json()['newboard']['grids'][0]
board = sudoku['value']
solution = sudoku['solution']
difficulty = sudoku['difficulty']
# pp(sudoku)
print("This is a randomly generated sudoku board from API with difficulty {}: ".format(difficulty))
pp(board)

while (board!=solution):
    user_row = input("Please select row (1-9) : ")
    user_col = input("Please select column (1-9) : ")
    user_num = input("Please enter number (1-9): ")
    board[int(user_row)-1][int(user_col)-1] = int(user_num)
    pp(board)
