from db.utils import get_score_info
from timedecorator import convert_secs_to_hhmmss


# gets player's name
def get_player_name():
    name = input("What is your name? ")
    return name


# get difficulty from user
def get_difficulty():
    difficulty = input("Please choose a difficulty from easy, medium and hard: ").lower()
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
                return 'pause'
            else:
                user_row = int(user_row)

        except (ValueError, TypeError):
            print("Invalid. Try again.")

    while not valid_number(user_col):
        try:
            user_col = input(" Please select column (1-9): ")
            if user_col == 'pause':
                return 'pause'
            else:
                user_col = int(user_col)

        except (ValueError, TypeError):
            print("Invalid. Try again.")

    while not valid_number(user_num):
        try:
            user_num = input(" Please enter number (1-9): ")
            if user_num == 'pause':
                return 'pause'
            else:
                user_num = int(user_num)

        except (ValueError, TypeError):
            print("Invalid. Try again.")

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
    scores = get_score_info(player_name)
    # If the player has no completed games we return an empty string
    if scores == None:
        return ""

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

        print("   ", item[0].title(), "|", convert_secs_to_hhmmss(item[1]), "|", str(score), "   ")

    return ""
