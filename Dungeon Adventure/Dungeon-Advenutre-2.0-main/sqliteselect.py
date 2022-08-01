import sqlite3
from sqlite3 import Error


class Select:
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
    def select_quiz_by_priority(conn, id):
        """
        Query quiz questions by id number
        :param conn: the Connection object
        :param id: the id of the quiz data
        :return: row with quiz data
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM quiz WHERE id=?", (id,))

        rows = cur.fetchone()
        return rows

    @staticmethod
    def selected_quiz(rows):
        """
        a method to return the data from def select_quiz_by_priority(conn, id)
        :param rows: the data to be returned
        :return: data from def select_quiz_by_priority(conn, id)
        """
        return rows

    @staticmethod
    def select_all_monsters(conn):
        """
        Query all rows in the monsters table
        :param conn: the Connection object
        :return: row with monster data for all monsters in db
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM monsters")

        rows = cur.fetchall()

        for row in rows:
            return row

    @staticmethod
    def select_monster(conn, monster):
        """
        Query monsters by priority
        :param conn: the Connection object
        :param monster: String emu, sphinx, phoenix, raven
        :return: row with monster data for specific monster in db
        """
        cur = conn.cursor()
        cur.execute("""SELECT * FROM monsters WHERE monsters=?""", (monster,))
        # I think so
        #
        rows = cur.fetchall()
        # create a function to query for each monster
        # pass in a specific variable and then query the monster name is a better version
        for row in rows:
            return row
