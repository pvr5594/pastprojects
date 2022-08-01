import sqlite3
from sqlite3 import Error

#run me first
#from https://www.sqlitetutorial.net/sqlite-python/

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"monsters.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS monsters (
                                        monsters text PRIMARY KEY,
                                        min_hp integer NOT NULL,
                                        max_hp integer NOT NULL,
                                        attack_min integer NOT NULL,
                                        attack_max integer NOT NULL,
                                        attack_speed integer NOT NULL,
                                        chance_to_hit_min integer NOT NULL,
                                        chance_to_hit_max integer NOT NULL,
                                        chance_to_hit integer NOT NULL,
                                        chance_to_dodge_min integer NOT NULL,
                                        chance_to_regenerate_min integer NOT NULL,
                                        chance_to_regenerate_max integer NOT NULL,
                                        regenerate_amount integer NOT NULL
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # # create tasks table
        # create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()