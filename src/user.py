# get difficulty from user
def get_difficulty():
    difficulty = input("Please select difficulty: ").lower()
    while not valid_difficulty(difficulty):
        difficulty = input("Invalid choice. Please select difficulty: ").lower()
    return difficulty


# check user choice of number valid
def valid_difficulty(difficulty):
    return difficulty in {"easy", "medium", "hard"}


def get_user_move():
    user_row = input(" Please select row (1-9): ")
    if user_row == 'exit':
        return 'exit'
    else:
        user_row = int(user_row)
    user_col = int(input(" Please select column (1-9): "))
    if user_col == 'exit':
        return 'exit'
    else:
        user_col = int(user_col)
    user_num = int(input(" Please enter number (1-9): "))
    if user_num == 'exit':
        return 'exit'
    else:
        user_num = int(user_num)

    while not valid_number(user_row):
        user_row = int(input(" Invalid choice of row, please try again: "))
    while not valid_number(user_col):
        user_col = int(input(" Invalid choice of column, please try again: "))
    while not valid_number(user_num):
        user_num = int(input(" Invalid choice of number, please try again: "))

    return user_row - 1, user_col - 1, user_num


# check user choice of number valid
def valid_number(number):
    return number in {1, 2, 3, 4, 5, 6, 7, 8, 9}
