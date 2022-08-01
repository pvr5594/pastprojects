import random
# from mock_game import MockGame as Game
from hero import Hero
from mockannouncement import MockAnnouncement as Announce


class Thief(Hero):
    """
    A class the handles information for the Thief
    """

    def __init__(self, name, game):
        super().__init__(name, game, 200, 250, 30, 66, 7, .90, .99, .5, .75, .2, .25)
        self.__game = game
        self.announce = Announce()

    """instantiation of clerics special move"""
    def special_move(self, defender):
        "checks to see if opponent is dead"
        if defender.get_current_hp() <= 0:
            defender.is_dead()

        second_chance_to_hit = (self.get_chance_to_hit()) / 2
        hitChance = random.uniform(.1, 1)
        damage = (self.get_attack_damage_range()) * 2

        "thief's special move does double damage but at half the accuracy"
        if second_chance_to_hit >= hitChance:
            new_hp = defender.get_current_hp()
            result = new_hp - damage

            if result >= defender.get_generated_hp():
                defender.set_current_hp(0)
            else:
                defender.set_current_hp(result)
            self.announce.announce(f"You used the Sneak Attack ability, and strike twice! It deals {damage} damage, "
                                   f"bringing your \nopponent's HP to {defender.get_current_hp()}.\n")
            self.announce.announce_monster_stats(f"{defender}")

            return True
        # "thief's special move ends up doing regular damage for a percentage"
        elif second_chance_to_hit >= hitChance / 2:
            new_hp = defender.get_current_hp()
            result = new_hp - (damage // 2)

            if result >= defender.get_generated_hp():
                defender.set_current_hp(0)
            else:
                defender.set_current_hp(result)
            self.announce.announce(f"You used the Sneak Attack ability, but you were spotted just in time! You strike "
                                   f"only once and deal {damage // 2} damage, bringing your "f"opponent's HP to \n"
                                   f"{defender.get_current_hp()}.\n")
            self.announce.announce_monster_stats(f"{defender}")

        # "thief's special move has a very small chance to miss and do 0 damage"
        else:
            self.announce.announce(f"You used the Sneak Attack ability and Missed! It deals {0} damage, bringing your "
                                   f"opponent's HP to \n{defender.get_current_hp()}.\n")
            return False

# thief = Thief("Kevin")
# print(thief)
#
# thief.special_move()
# thief.special_move()
# thief.special_move()
# thief.special_move()
# thief.special_move()
# thief.special_move()
# thief.special_move()
#
# print(thief)
#
# thief.add_health_potion()
# thief.use_health_potion()
#
# print(thief)
