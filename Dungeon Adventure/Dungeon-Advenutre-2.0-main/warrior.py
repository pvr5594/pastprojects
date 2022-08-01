import random
# from mock_game import MockGame as Game
from hero import Hero
from mockannouncement import MockAnnouncement as Announce


class Warrior(Hero):
    """
    A class the handles information for the Warrior
    """

    def __init__(self, name, game):
        super().__init__(name, game, 200, 300, 30, 90, 4, .70, .80, .3, .4, .30, .5)
        self.__game = game
        self.announce = Announce()

    def special_move(self, defender):
        if self.get_current_hp() <= 0:
            self.is_dead()

        reduced_chance_to_hit = (self.get_chance_to_hit()) / 2
        hitChance = random.uniform(.1, 1)
        damage = (self.get_attack_damage_range()) * 3

        if reduced_chance_to_hit >= hitChance:
            new_hp = defender.get_current_hp()
            result = new_hp - damage

            if result >= defender.get_generated_hp():
                defender.set_current_hp(0)
                self.announce.announce(f"{self.get_name()} used the Crushing Blow ability! It deals {damage} damage, "
                                       f"bringing {defender.get_name()} HP to {defender.get_current_hp()}.\n")
                self.announce.announce_monster_stats(f"{defender}")
            else:
                defender.set_current_hp(result)
                self.announce.announce(f"{self.get_name()} used the Crushing Blow ability! It deals {damage} damage, "
                                     f"bringing {defender.get_name()} HP to {defender.get_current_hp()}.\n")
                self.announce.announce_monster_stats(f"{defender}")
            return True
        else:
            self.announce.announce(f"{self.get_name()} used the Crushing Blow ability and Missed! It deals {0} damage, "
                                 f"bringing {defender.get_name()}  HP to {defender.get_current_hp()}.\n")
            return False


# adventurer = Warrior("Pranav", Game())
# me = Warrior("Kevin", Game())
# print(adventurer)
# print(me)
#
# me.fight(me, adventurer)
# me.special_move()
#
# print(adventurer)
# print(me)

# print("my name is ", adventurer.get_name())
# print(me)
#
# me.special_move()
# me.special_move()
# me.special_move()
# me.special_move()
# me.special_move()
# print(me)


# print("\n------------------------print adventurer status ('empty', try using either potion)-------------------------")
# adventurer.use_health_potion()
# adventurer.use_vision_potion()
#
# print(adventurer)
#
# print("\n------------------------print adventurer status (+1 potion)-------------------------")
# adventurer.add_health_potion()
# print(adventurer)
#
# print("\n------------------------print adventurer status (take damage 1st)-------------------------")
# adventurer.take_damage(1, "angry gnat")
# print(adventurer)
#
# print("\n------------------------print adventurer status (take 1st health potion)-------------------------")
# adventurer.use_health_potion()
# print(adventurer)
#
#
# print("\n------------------------print adventurer status (Add two of each potion)-------------------------")
# adventurer.add_health_potion()
# adventurer.add_health_potion()
# adventurer.add_vision_potion()
# adventurer.add_vision_potion()
#
# print(adventurer)
#
#
# print("\n------------------------print adventurer status (Add 'A' to the Pillars + adding an extra 'A' and a false 'z')"
#       "-------------------------")
# adventurer.earn_pillar("A")
# try:
#     adventurer.earn_pillar("A")
#     print("should have failed.")
# except:
#     pass
#
# try:
#     adventurer.earn_pillar("z")
#     print("should have failed.")
# except:
#     pass
#
#
# print(adventurer)
#
#
#
# print("\n------------------------print adventurer status (TIME TO DIE!!!)-------------------------")
# print(adventurer)
# adventurer.take_damage(2000, "extra legendary pit")
# print(adventurer)
#
#
#
# print("\n------------------------print adventurer exit (doesn't have all Pillars of OO)-------------------------\n")
# adventurer.exit()
#
# print(adventurer)
#
#
#
# print("\n------------------------print adventurer status (Add 'E', 'I', 'P')-------------------------")
# adventurer.earn_pillar("P")
# adventurer.earn_pillar("I")
# adventurer.earn_pillar("E")
#
# print(adventurer)
#
# print("\n------------------------print adventurer exit (has all Pillars of OO)-------------------------\n")
# adventurer.exit()
