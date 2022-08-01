import sqlite3
from sqlite3 import Error


class Update:
    @staticmethod
    def create_connection(db_file):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

    @staticmethod
    def update_task(conn, updates):
        """
        update quiz questions selected
        :param conn: connection to database
        :param updates: updates to be made
        :return: project id
        """
        sql = ''' UPDATE quiz
                  SET category = ? ,
                      question = ? ,
                      answer = ?
                  WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, updates)
        conn.commit()

