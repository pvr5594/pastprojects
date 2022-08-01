
from monster import Monster
from sqliteselect import Select

"""
self, name, min_hp, max_hp, generated_hp, current_hp, attack_min, attack_max, attack_damage_range,
                 attack_speed, chance_to_hit_min, chance_to_hit_max, chance_to_hit, chance_to_dodge_min,
                 chance_to_dodge_max, chance_to_dodge, chance_to_regenerate_min, chance_to_regenerate_max,
                 regenerate_amount
"""


class Sphinx(Monster):
    def __init__(self, diff, name=None, game=None):
        database = r"monsters.db"
        s = Select
        # create a database connection
        conn = s.create_connection(database)
        with conn:
            print("1. Query task by priority:")
            # select_monster(conn, 'sphinx')
            monster_data = s.select_monster(conn, 'sphinx')
        print(monster_data[0])  # access each number individually

        super().__init__(monster_data[0], game, monster_data[1], monster_data[2], monster_data[3],
                         monster_data[4], monster_data[5], monster_data[6], monster_data[7],
                         monster_data[8], monster_data[9], monster_data[10], monster_data[11], monster_data[12])

        self.__diff = diff
        self.__name = name

    def get_diff(self):
        self.__diff.get()

    # overriding 'name' method
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = "Sphinx"


if __name__ == "__main__":
    test = Sphinx(10)