import unittest

from src.db.connect import _connect_to_db


class dbConnectionTest(unittest.TestCase):

    # test to check the connection to the database
    def test_connection_to_db(self):
        connection = _connect_to_db()
        self.assertTrue(connection.is_connected())


if __name__ == '__main__':
    unittest.main()
