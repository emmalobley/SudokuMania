from src.db.connect import _connect_to_db


class DbConnectionError(Exception):
    pass


def save_player(player_name):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()

        query = """INSERT INTO player({}) VALUES('{}')""".format("Player_name", player_name)
        cur.execute(query)
        db_connection.commit()
        cur.close

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()

    print("Player {} added to DB".format(player_name))


def get_player_id(player_name):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()

        # check this query in python:
        query = """SELECT  p.player_id
                FROM player p
                WHERE p.player_name = '{}'""".format(player_name)

        cur.execute(query)
        result = cur.fetchall()  # check is fetchall is correct or if it's fetchmany

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()

    if not result:
        print("This user does not exist")
        return
    # returns player id
    return result[0][0]


def save_board_to_db(boards_data):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Saving board to DB: sudoku")

        # change cast based on time format
        query = ("""INSERT INTO boards({}) VALUES
                ({}, '{}', '{}', CAST('{}' AS TIME(0)), '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
            ','.join(boards_data.keys()),
            boards_data['player_id'],
            boards_data['difficulty'],
            boards_data['completed'],
            boards_data['total_time'],
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


def get_unfinished_board(player_name):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()

        # check this query in python:
        query = """SELECT  b.difficulty, TIME_TO_SEC(b.total_time),
                        b.row_1, b.row_2, b.row_3, b.row_4,
                        b.row_5, b.row_6, b.row_7, b.row_8, b.row_9
                FROM player p INNER JOIN boards b ON p.player_id = b.player_id
                WHERE p.player_name = '{}' AND b.completed = False""".format(player_name)

        cur.execute(query)
        result = cur.fetchall()  # check is fetchall is correct or if it's fetchmany

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()

    if not result:
        # no unfinished puzzles
        return
    # returns most recent unfinished board for that user
    return result[-1]


# returns difficulties and timestamps for completed boards for given user
def get_score_info(player_name):
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()

        # check this query in python:
        query = """SELECT  b.difficulty, TIME_TO_SEC(b.total_time)
                FROM boards b INNER JOIN player p ON b.player_id = p.player_id
                WHERE p.player_name = '{}' AND b.completed = True
                 ORDER BY 
                 CASE difficulty
                 WHEN 'easy' THEN 1
                  WHEN 'medium' THEN 2
                   WHEN 'hard' THEN 3
                    END, total_time""".format(player_name)

        cur.execute(query)
        result = cur.fetchall()  # check is fetchall is correct or if it's fetchmany

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()

    if not result:
        print("No completed puzzles for this user")
        return

    return result


if __name__ == '__main__':
    print(get_score_info("Jane"))
    pass
