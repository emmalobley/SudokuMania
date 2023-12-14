from src.db.connect import _connect_to_db

class DbConnectionError(Exception):
    pass


def save_player(player_name):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: sudoku")

        query = """INSERT INTO player({}) VALUES('{}')""".format("Player_name", player_name)
        cur.execute(query)
        db_connection.commit()
        cur.close

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("Db connection is closed")

    print("Player {} added to DB".format(player_name))


# maybe change player_time table to also include the board difficult?
def save_player_time(time):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: sudoku")

        query = """INSERT INTO player_time({}) VALUES('{}')""".format('total_time', time)
        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("Db connection is closed")

    print("Time {} added to DB".format(time))


def save_to_boards_table(boards_data):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: sudoku")

        query = ("""INSERT INTO boards({}) VALUES
                ({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
            ','.join(boards_data.keys()),
            boards_data['player_id'],
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
            boards_data['row_9'],
        ))
        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("Db connection is closed")


def get_unfinished_boards(player_name):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: sudoku")

        # check this query in python:
        query = """SELECT p.player_name, 
                        b.row_1, b.row_2, b.row_3, b.row_4,
                        b.row_5, b.row_6, b.row_7, b.row_8, b.row_9
                FROM player p INNER JOIN boards b ON p.player_id = b.player_id
                WHERE p.player_name = {} AND b.completed = false""".format(player_name)

        try:
            cur.execute(query)
            result = cur.fetchall()  # check is fetchall is correct or if it's fetchmany

            # to print each row on a new line:
            for i in result:
                print(i)

        except Exception:
            print("No unfinished puzzles for this user")
            result = 0

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("Db connection is closed")

    return result


if __name__ == '__main__':
    pass
