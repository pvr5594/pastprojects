from hero import Hero
from mockannouncement import MockAnnouncement as Announce


class Cleric(Hero):
    """
    A class the handles information for the Cleric
    """
    def __init__(self, name, game):
        super().__init__(name, game, 200, 275, 40, 77, 5, .80, .90, .4, .6, .30, .4)
        self.__game = game
        self.announce = Announce()

    """instantiation of clerics special move"""
    def special_move(self, defender):
        heal = 66
        new_hp = self.get_current_hp() + heal

        if new_hp >= self.get_generated_hp():
            self.set_current_hp(self.get_generated_hp())
        else:
            self.set_current_hp(new_hp)
        self.announce.announce(f"You used the Heal ability! It heals {heal} HP, bringing you to {self.get_current_hp()}.\n")
        self.announce.announce_hero_stats(f"{defender}")
        return True


# adventurer = Cleric("Talia")
# print(adventurer)
#
#
# print("\n------------------------print adventurer status ('empty', try using either potion)-------------------------")
# adventurer.use_health_potion()
# adventurer.use_vision_potion()
#
# adventurer.take_damage(99, "Phoenix")
#
# print(adventurer)
#
# adventurer.special_move()
# adventurer.special_move()
# adventurer.special_move()
#
#
# print(adventurer)


