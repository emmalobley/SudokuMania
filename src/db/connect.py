import mysql.connector
from src.db.config import HOST, USER, PASSWORD, DATABASE


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

