import mysql.connector
from src.db.config import HOST, USER, PASSWORD, DATABASE


class DbConnectionError(Exception):
    pass


# function to connect to the db using the user's details stored in the config file
# which is imported above
def _connect_to_db():
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='my_sql_native_password',
        database=DATABASE
    )
    return cnx


# dummy data to test add_player function
name = "Jane"


def add_player(player_name):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = """INSERT INTO player ({}) VALUE ('{}')""".format("Player_name", player_name)
        cur.execute(query)
        db_connection.commit()
        cur.close()

        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    except Exception:
        raise DbConnectionError("Failed to read data from DB")


    print("Player added to DB")


# dummy data to test insert_new_board function
sudoku_board = {
    'player_id': '1',
    'Difficulty': 'Easy',
    'Completed': 'TRUE',  # this is stored as 1 in sql (0 is boolean false)
    'Row_1': "0, 2, 1, 0, 9, 0, 5, 0, 0",
    'Row_2': "5, 7, 9, 0, 8, 4, 0, 2, 0",
    'Row_3': "6, 8, 4, 3, 2, 5, 0, 7, 9",
    'Row_4': "1, 4, 2, 0, 0, 9, 0, 0, 0",
    'Row_5': "7, 9, 3, 5, 0, 8, 2, 4, 1",
    'Row_6': "0, 5, 6, 4, 1, 2, 9, 0, 7",
    'Row_7': "9, 6, 0, 2, 7, 0, 4, 5, 0",
    'Row_8': "4, 1, 0, 0, 5, 3, 6, 9, 2",
    'Row_9': "2, 0, 5, 9, 4, 0, 7, 0, 8"
}


def insert_new_board(board):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = (
            """INSERT INTO boards ({}) VALUES ({}, '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"""
            .format(', '.join(board.keys()),
                    board['player_id'],
                    board['Difficulty'],
                    board['Completed'],
                    board['Row_1'],
                    board['Row_2'],
                    board['Row_3'],
                    board['Row_4'],
                    board['Row_5'],
                    board['Row_6'],
                    board['Row_7'],
                    board['Row_8'],
                    board['Row_9'],
                    ))
        cur.execute(query)
        db_connection.commit()
        cur.close()

        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    except Exception:
        raise DbConnectionError("Failed to read data from DB")


    print("Board added to DB")


# function to retrieve all existing boards
def get_boards():
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = """SELECT board_id, Difficulty, Completed, Row_1, Row_2, Row_3, Row_4,
    Row_5, Row_6, Row_7, Row_8, Row_9 FROM boards"""
        cur.execute(query)
        result = cur.fetchall()

        for i in result:
            # print(i)
            if i[2] == 1:
                print("Board {} is completed!".format(i[0]))  # completed
            else:
                print("Board {} incomplete".format(i[0]))

        cur.close()

        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    except Exception:
        raise DbConnectionError("Failed to read data from DB")


    return result


def main():
    add_player(name)
    insert_new_board(sudoku_board)
    get_boards()


if __name__ == '__main__':
    main()
