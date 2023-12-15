from db.utils import save_player


# gets player's name
def get_player_name():
    name = input("What is your name? ")
    return name


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
    user_row = ""
    user_col = ""
    user_num = ""
    while not valid_number(user_row):
        try:
            user_row = input(" Please select row (1-9): ")
            if user_row == 'pause':
                return 'exit'
            else:
                user_row = int(user_row)

        except (ValueError, TypeError):
            print("Invalid. Try again.")

    while not valid_number(user_col):
        try:
            user_col = input(" Please select column (1-9): ")
            if user_col == 'pause':
                return 'exit'
            else:
                user_col = int(user_col)

        except (ValueError, TypeError):
            print("Invalid. Try again.")

    while not valid_number(user_num):
        try:
            user_num = input(" Please enter number (1-9): ")
            if user_num == 'pause':
                return 'exit'
            else:
                user_num = int(user_num)

        except (ValueError, TypeError):
            print("Invalid. Try again.")

    return user_row - 1, user_col - 1, user_num


# check user choice of number valid
def valid_number(number):
    return number in {1, 2, 3, 4, 5, 6, 7, 8, 9}


# function to get user name - savew to db using save_player(player_name)