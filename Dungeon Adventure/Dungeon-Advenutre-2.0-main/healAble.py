from dungeonCharacter import DungeonCharacter
# from hero import Hero
import random


class HealAble():
    def heal(self):
        heal = 40

        new_hp = self.get_current_hp() + heal

        if new_hp >= self.get_generated_hp():
            self.set_current_hp(self.get_generated_hp())
        else:
            self.set_current_hp(new_hp)

        print(f"Used a health potion! It heals {heal} HP, bringing you to {self.get_current_hp()}.")
        # self.__game.announce(f"Used a health potion! It heals {heal} HP, bringing you to {self.__current_hp}.")
        return True


# a = HealAble("Kevin", 100, 200, 30, 80, 4, .60, .75, random.uniform(.60, .75), .20, .30, random.uniform(.20, .30), .30,
#              .50, random.uniform(.30, .50))
#
# print(a)
#
# a.take_damage(100, "pit")
#
# print(a)
#
# a.heal()
#
# print(a)
#
#
