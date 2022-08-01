from dungeonCharacter import DungeonCharacter
import random
from mockannouncement import MockAnnouncement as Announce


class Monster(DungeonCharacter):
    def __init__(self, name, game, min_hp, max_hp, attack_min, attack_max, attack_speed, chance_to_hit_min,
                 chance_to_hit_max, chance_to_hit, chance_to_dodge_min, chance_to_regenerate_min,
                 chance_to_regenerate_max, regenerate_amount):
        super().__init__(name, game, min_hp, max_hp, attack_min, attack_max, attack_speed, chance_to_hit_min,
                         chance_to_hit_max, chance_to_hit, chance_to_dodge_min)

        self.__game = game
        self.announce = Announce()

        self.__chance_to_regenerate_min = chance_to_regenerate_min
        self.__chance_to_regenerate_max = chance_to_regenerate_max
        self.__chance_to_regenerate = random.uniform(self.__chance_to_regenerate_min, self.__chance_to_regenerate_max)
        self.__regenerate_amount = regenerate_amount

    """getters and setters specific for monster class and it's children"""
    def get_chance_to_regenerate_min(self):
        return self.__chance_to_regenerate_min

    def set_chance_to_regenerate_min(self, regenerate_min):
        self.__chance_to_regenerate = regenerate_min

    def get_chance_to_regenerate_max(self):
        return self.__chance_to_regenerate_max

    def set_chance_to_regenerate_max(self, regenerate_max):
        self.__chance_to_regenerate_max = regenerate_max

    def regen_chance_compare(self):
        regen_chance = random.uniform(.1, 1)
        return regen_chance

    def get_regenerate_amount(self):
        return self.__regenerate_amount

    def set_regenerate_amount(self, regen_amount):
        self.__regenerate_amount = regen_amount

    """ability to regenerate HP"""
    def regenerate(self):
        announcement = self.announce

        current_hp = self.get_current_hp()
        new_hp = current_hp + self.__regenerate_amount

        if self.get_current_hp() <= 0:
            self.is_dead()

            if new_hp >= self.get_generated_hp():
                self.set_current_hp(self.get_generated_hp())
                announcement.announce(f"{self.get_name()} Managed to regenerate! However, {self.get_name()} has max HP "
                                      f"so it only heals {0} HP, bringing it to {self.get_current_hp()}.\n")
            else:
                self.set_current_hp(new_hp)
                announcement.announce(f"{self.get_name()} Managed to regenerate! It heals {self.__regenerate_amount} HP,"
                                     f" bringing it to {new_hp}.\n")
            return True

    """produces the string stats for dungeon character and monster (this will be carried over into it's children)"""
    def __str__(self):
        prefix = super().__str__()
        line1 = str(prefix[0])
        line2 = str(prefix[1])
        line3 = str(prefix[2])
        line4 = str(prefix[3])
        line5 = str(prefix[4])
        line6 = str(prefix[5])

        regen_range_str = f"Regen Chance: {round(self.__chance_to_regenerate_min * 100)}% to " \
                          f"{round(self.__chance_to_regenerate_max * 100)}% "
        regen_amount_str = f"Regen Amount: {self.__regenerate_amount} "
        status_items = [line1, line2, line3, line4, line5, line6, regen_range_str, regen_amount_str]

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

    def take_damage(self, damage, source):
        announcement = self.announce
        if self.get_current_hp() > 0:
            self.is_dead()

        if self.__chance_to_regenerate >= self.regen_chance_compare():
            self.regenerate()
            announcement.announce(f"\nRegen Sucessful:\n{self.get_name()} Managed to regenerate! It heals "
                                  f"{self.__regenerate_amount} HP, bringing {self.get_name()} to "
                                  f"{self.get_current_hp()}.\n")
        else:
            announcement.announce(f"\nRegen Failed:\n{self.get_name()} failed to regenerate! It heals {0} HP, bringing "
                                  f"{self.get_name()} to {self.get_current_hp()}.\n")
        super().take_damage(damage, source)



# jack = Monster("Jack", Game(), 200, 300, 40, 80, 4, .70, .85, .60, .80, .60, .80, 60)
# jill = Monster("Jill", Game(), 100, 200, 30, 80, 3, .30, .65, .20, .30, .2, .3, 20)
# jack.fight(jack, jill)


# print(c)f
#
# c.take_damage(100, "Hero")
#
# print(c)
#
# c.regenerate()
#
# print(c)
