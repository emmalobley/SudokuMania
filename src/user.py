from db.utils import save_player, get_score_info


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
    user_row = input(" Please select row (1-9): ")
    if user_row == 'exit':
        return 'exit'
    elif user_row == 'restart':
        return 'restart'
    else:
        user_row = int(user_row)
    user_col = int(input(" Please select column (1-9): "))
    if user_col == 'exit':
        return 'exit'
    elif user_col == 'restart':
        return 'restart'
    else:
        user_col = int(user_col)
    user_num = int(input(" Please enter number (1-9): "))
    if user_num == 'exit':
        return 'exit'
    elif user_num == 'restart':
        return 'restart'
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



# wrapper for scoreboard
def pretty_scoreboard(func):
    def wrapper(*args, **kwargs):

        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("       SCOREBOARD:         ")
        print("---------------------------")
        print(" Difficulty | Time | Score ")
        print("---------------------------")
        print(func(*args, **kwargs))
        print("---------------------------")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")

        return

    return wrapper

# function to get user  - present relevant info in scoreboard
@pretty_scoreboard
def get_user_score(player_name):
    # player_scores = get_score_info(player_name)
    scores = [('hard', 1202), ('easy', 322)]  # from db in this form?
    for item in scores:
        score = 1800 - item[1]  # 30 minutes minus time taken
        # if over 30 minutes then score zero
        if score < 0:
            score = 0

        if item[0] == "easy":
            score = score + 100
        elif item[0] == "medium":
            score = score + 300
        elif item[0] == "hard":
            score = score + 500

        print("   ", item[0].title(), "|", str(item[1]), "|", str(score), "   ")

    return ""


get_user_score("Jane")
