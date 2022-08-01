import sqlite3
from sqlite3 import Error

#run me fourth
#from https://www.sqlitetutorial.net/sqlite-python/

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


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM monsters")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_monster(conn, monster):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param monster: String emu, sphinx, phoenix, raven
    :return:
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


def main():
    database = r"monsters.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
        select_monster(conn, 1)

        print("2. Query all tasks")
        select_all_tasks(conn)


# if __name__ == '__main__':
#     main()