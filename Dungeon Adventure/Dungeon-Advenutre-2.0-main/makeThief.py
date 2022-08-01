
class MakeThief:
    def __user_input_adventurer_name(self):

        # numbers_only = re.compile("[0-9]*")
        # attempt_difficulty = diff.get()
        # if numbers_only.fullmatch(attempt_difficulty):
        #     self.__diff = int(diff.get())
        # else:
        #     print("Use numbers ya goof")
        #     return

        # if 4 > int(self.__diff) > 0:
        self.__warrior = Warrior(hero_name.get(), self)
        self.__reset_start_canvas("assets_background.png")
        self.__start_game()
        return

        self.__warrior = Cleric(hero_name.get(), self)
        self.__reset_start_canvas("assets_background.png")
        self.__start_game()
        return

        self.__warrior = Thief(hero_name.get(), self)
        self.__reset_start_canvas("assets_background.png")
        self.__start_game()
        return
        # else:
        #     print("Please enter a difficulty between 1 and 3.")