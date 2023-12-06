import mysql.connector
from db_config import HOST, USER, PASSWORD, DATABASE

#function to connect to the db using the user's details stored in the cofig file
#which is imported above
def _connect_to_db():
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='my_sql_native_password',
        database=DATABASE
    )
    return cnx

