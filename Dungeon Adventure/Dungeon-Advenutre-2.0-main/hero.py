import sys
from abc import ABCMeta, abstractmethod
from dungeonCharacter import DungeonCharacter
# from mock_game import MockGame as Game
from mockannouncement import MockAnnouncement as Announce

import random


class Hero(DungeonCharacter):
    def __init__(self, name, game, min_hp, max_hp, attack_min, attack_max, attack_speed, chance_to_hit_min,
                 chance_to_hit_max, chance_to_dodge_min, chance_to_dodge_max, chance_to_block_min, chance_to_block_max):
        super().__init__(name, game, min_hp, max_hp, attack_min, attack_max, attack_speed, chance_to_hit_min,
                         chance_to_hit_max, chance_to_dodge_min, chance_to_dodge_max)
        self.__game = game
        self.__chance_to_block_min = chance_to_block_min
        self.__chance_to_block_max = chance_to_block_max
        self.__chance_to_block = random.uniform(self.__chance_to_block_min, self.__chance_to_block_max)
        self.__pillars = []
        self.__MAXPILLARS = 4
        self.__vision_p = 0
        self.__health_p = 0
        self.__vision = 0
        self.announce = Announce()

    def get_chance_to_block_min(self):
        return self.__chance_to_block_min

    def set_chance_to_block_min(self, block_min):
        self.__chance_to_block_min = block_min

    def get_chance_to_block_max(self):
        return self.__chance_to_block_max

    def set_chance_to_block_max(self, block_max):
        self.__chance_to_block_max = block_max

    def get_chance_to_block(self):
        return self.__chance_to_block

    def set_chance_to_block(self, block_chance):
        self.__chance_to_block = block_chance

    """abstract method that will be carried over to child classes. reason being that even though all child classes will" \
    "have aspecial_move, they will operate very differently from each other"""
    @abstractmethod
    def special_move(self, defender):
        pass

    def earn_pillar(self, pillar):
        """
        Called by Room to add pillars to Hero's inventory.
        """

        if pillar == "A" or pillar == "E" or pillar == "I" or pillar == "P":
            self.__pillars.append(pillar)
            self.__game.announce(f"Earned a pillar!  You now have {self.__pillars}")

        else:
            raise Exception("The pillar value <" + pillar + "> is neither 'A', 'E', 'I', or 'P'!!!")

    def add_health_potion(self):
        """
        Increments health potion count by 1.
        """
        self.__health_p += 1
        self.__game.announce(f"You pick up a health potion.\nYou now have {self.__health_p} of them.")
        return self.__health_p

    def use_health_potion(self):
        """
        If the Hero has any health potions, uses one and increases
        Hero's health by a random number.
        :returns: True if potion was used, False otherwise
        """
        announcement = self.announce
        heal = 50

        if self.__health_p > 0:
            self.__health_p -= 1
            new_hp = self.get_current_hp() + heal

            if new_hp >= self.get_generated_hp():
                self.set_current_hp(self.get_generated_hp())
            else:
                self.set_current_hp(new_hp)

            self.__game.announce(
                f"{self.get_name()} a health potion! It heals {heal} HP, bringing you to {self.get_current_hp()}.")
            announcement.announce(
                f"{self.get_name()} a health potion! It heals {heal} HP, bringing you to {self.get_current_hp()}.")

            return True

        elif self.__health_p <= 0:
            self.__game.announce(f"{self.get_name()} reach for a health potion and find only disappointment.")
            announcement.announce(f"{self.get_name()} reach for a health potion and find only disappointment.")

            return False

    def add_vision_potion(self):
        """
        Increments vision potion count by 1.
        """
        self.__vision_p += 1
        self.__game.announce(f"You pick up a vision potion.\nYou now have {self.__vision_p} of them.")
        return self.__vision_p

    def use_vision_potion(self):
        """
        Uses a vision potion if the Hero has one.
        :returns: True if potion used, False otherwise.
        """
        if self.__vision_p > 0:
            self.__vision_p -= 1
            self.__vision += 2

            self.__game.announce(f"Your vision has temporarily increased to {self.__vision}!")
            return True

        else:
            self.__game.announce("You look for a vision potion but don't see one.")
            return False

    def get_vision_range(self):
        """
        Returns vision range of Hero.
        """
        return self.__vision

    def decay_vision(self):
        """
        Reduces vision by 1 if it's above 0.
        """
        if self.__vision > 0:
            self.__vision -= 1

            self.__game.announce("The effects of your vision potion fade a little.")

    def exit(self):
        """
        Ends the game if the Hero has all four pillars, or if they run out of HP.  Makes an announcement either way.
        """
        if len(self.__pillars) >= self.__MAXPILLARS:
            self.__game.end_game()
            return
        elif self.get_current_hp() <= 0:
            self.__game.end_game()
            return
        else:
            self.__game.announce("You feel like you could escape from\nthis room if only you knew more\nabout "
                                 "programming.")
            return

    def take_damage(self, damage, source):
        announcement = self.announce

        chance = random.uniform(.1, 1)

        if self.__chance_to_block >= chance:
            announcement.announce(f"Block Successful")
            super().take_damage(0, source)
            announcement.announce(f"\n")
        else:
            announcement.announce(f"Block Failed")
            super().take_damage(damage, source)
            announcement.announce(f"\n")

    """produces the string stats for dungeon character and hero (this will be carried over into it's children)"""
    def __str__(self):
        """
        Returns a string representation of the Hero.
        """
        prefix = super().__str__()
        line1 = str(prefix[0])
        line2 = str(prefix[1])
        line3 = str(prefix[2])
        line4 = str(prefix[3])
        line5 = str(prefix[4])
        line6 = str(prefix[5])

        block_str = f"Block Chance: {round(self.__chance_to_block_min * 100)}% to {round(self.__chance_to_block_max * 100)}% "
        healthp_str = f"Health potions: {self.__health_p}"
        visionp_str = f"Vision potions: {self.__vision_p}"
        pillar_string = f"Pillars found: {self.__pillars}"

        status_items = [line1, line2, line3, line4, line5, line6, block_str, healthp_str, visionp_str, pillar_string]

        line_size = 0
        for line in status_items:
            if len(line) > line_size:
                line_size = len(line)

        # create borders
        border = "+" + "-" * (line_size + 2) + "+"

        # add spacers to all status items based on max length
        # so that right border is even
        output_str = "\n" + border
        for line in status_items:
            output_str += f"\n| {line}"
            white_space = line_size - len(line)
            if white_space > 0:
                output_str += " " * white_space
            output_str += " |"

        output_str += f"\n{border}\n"

        return output_str

    # debug code, only used for unit tests
    def is_pillar_in_inventory(self, pillar):
        return pillar in self.__pillars



# kevin = Hero("Kevin", Game(), 200, 300, 40, 80, 4, .70, .85, .30, .40, .50, 75)
# talia = Hero("Talia", Game(), 100, 200, 30, 80, 3, .30, .65, .20, .30, .2, .3)
# kevin.fight(kevin, talia)

#
# print("\n------------------------print adventurer status ('empty', try using either potion)-------------------------")
# b.use_health_potion()
# b.use_vision_potion()
#
# print(b)
#
# print("\n------------------------print adventurer status (+1 potion)-------------------------")
# b.add_health_potion()
# print(b)
#
# print("\n------------------------print adventurer status (take damage 1st)-------------------------")
# b.take_damage(1, "angry gnat")
# print(b)
#
# print("\n------------------------print adventurer status (take 1st health potion)-------------------------")
# b.use_health_potion()
# print(b)


# print("\n------------------------print adventurer status (Add two of each potion)-------------------------")
# b.add_health_potion()
# b.add_health_potion()
# b.add_vision_potion()
# b.add_vision_potion()
#
# print(b)
#
#
# print("\n------------------------print adventurer status (Add 'A' to the Pillars + adding an extra 'A' and a false 'z')"
#       "-------------------------")
# b.earn_pillar("A")
# try:
#     b.earn_pillar("A")
#     print("should have failed.")
# except:
#     pass
#
# try:
#     b.earn_pillar("z")
#     print("should have failed.")
# except:
#     pass
#
#
# print(b)
#
#
#
# print("\n------------------------print adventurer status (TIME TO DIE!!!)-------------------------")
# print(b)
# b.take_damage(20, "legendary pit")
# b.take_damage(20, "legendary pit")
# b.take_damage(20, "legendary pit")
# b.take_damage(20, "legendary pit")
# b.take_damage(20, "legendary pit")
# b.take_damage(2000, "extra legendary pit")
# print(b)
#
#
#
# print("\n------------------------print adventurer exit (doesn't have all Pillars of OO)-------------------------\n")
# b.exit()
#
# print(b)
#
#
#
# print("\n------------------------print adventurer status (Add 'E', 'I', 'P')-------------------------")
# b.earn_pillar("P")
# b.earn_pillar("I")
# b.earn_pillar("E")
#
# print(b)
#
# print("\n------------------------print adventurer exit (has all Pillars of OO)-------------------------\n")
# b.exit()
