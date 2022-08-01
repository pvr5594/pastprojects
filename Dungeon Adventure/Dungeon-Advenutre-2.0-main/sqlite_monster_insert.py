import sqlite3
from sqlite3 import Error

#run me second
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
    except Error as e:
        print(e)

    return conn


def create_project(conn, monsters):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO monsters(monsters, min_hp, max_hp, attack_min, attack_max, attack_speed, chance_to_hit_min, chance_to_hit_max,
                 chance_to_hit, chance_to_dodge_min, chance_to_regenerate_min,
                 chance_to_regenerate_max, regenerate_amount)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    # cur.execute(sql, monsters)
    cur.execute("INSERT INTO monsters VALUES ('emu', 250, 333, 33, 44, 3, .60, .75, .3, .5, .30, .5, 20)")
    cur.execute("INSERT INTO monsters VALUES ('phoenix', 250, 333, 40, 60, 1, .40, .60, .10, .25, .10, .20, 20)")
    cur.execute("INSERT INTO monsters VALUES ('raven', 100, 120, 40, 60, 1, .40, .60, .10, .25, .10, .20, 20)")
    # cur.execute("INSERT INTO monsters VALUES ('sphinx', 250, 333, 40, 60, 1, .40, .60, .10, .25, .10, .20, 20)")
    conn.commit()
    return cur.lastrowid


def main():
    database = r"monsters.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        monsters = (('emu', 250, 333, 33, 44, 3, .60, .75, .3, .5, .30, .5, 20),
                    ('phoenix', 250, 333, 40, 60, 1, .40, .60, .10, .25, .10, .20, 20),
                    ('raven', 100, 120, 40, 60, 1, .40, .60, .10, .25, .10, .20, 20),
                    ('sphinx', 250, 333, 40, 60, 1, .40, .60, .10, .25, .10, .20, 20))
        project_id = create_project(conn, monsters)
        # for monster in monsters:
        #     project_id = create_project(conn, monster)


if __name__ == '__main__':
    main()