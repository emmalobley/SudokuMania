from connect import _connect_to_db
from main import get_difficulty
class DbConnectionError(Exception):
    pass

def save_player(player_name):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: sudoku")

        query = """INSERT INTO player({}) VALUES('{}')""".format(
            ','.join(player_name.keys()),
            player_name['player_name']
        )
        cur.execute(query)
        db_connection.commit()
        cur.close

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("Db connection is closed")

def save_player_time(time):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: sudoku")

        query = """INSERT INTO player({}) VALUES('{}')""".format(
            ','.join(time.keys()),
            time['total_time']
        )
        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("Db connection is closed")

def save_to_boards_table(boards_data):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: sudoku")

        query = """INSERT INTO boards({}) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', )""".format(
            ','.join(boards_data.keys()),
            boards_data['difficulty'],
            boards_data['completed'],
            boards_data['row_1'],
            boards_data['row_2'],
            boards_data['row_3'],
            boards_data['row_4'],
            boards_data['row_5'],
            boards_data['row_6'],
            boards_data['row_7'],
            boards_data['row_8'],
            boards_data['row_9']
        )
        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("Db connection is closed")


# def sudoku_board():
#     try:
#         db_connection = _connect_to_db()
#         cur = db_connection.cursor()
#         print("Connected to DB: sudoku")
#
            # figure out how to write this query in python:
#         query = """SELECT p.player_name,
#                         b.row_1,
#                         b.row_2,
#                         b.row_3,
#                         b.row_4,
#                         b.row_5,
#                         b.row_6,
#                         b.row_7,
#                         b.row_8,
#                         b.row_9
#                 FROM player p
#                 INNER JOIN boards b ON p.player_id = b.player_id
#                 WHERE b.completed = False;"""
#
#         cur.execute(query)
#         db_connection.commit()
#         result = cur.fetchall() #check is fetchall is correct or if it's fetchmany
#
#         #to print each row on a new line:
#         for i in result:
#             print(i)
#         cur.close()
#
#     except Exception:
#         raise DbConnectionError("Failed to read data from DB")
#
#     finally:
#         if db_connection:
#             db_connection.close()
#             print("Db connection is closed")


def main():
    pass

if __name__ == '__main__':
    main()