from observer import Observer


class BadGuy(Observer):
    """
    Reacts to the observable it has been attached to.
    Credit https://www.c-sharpcorner.com/article/observer-design-pattern-exaple-with-python-sample/
    Credit https://en.proft.me/2017/02/21/observer-pattern-java-and-python/
    """
    def update(self, observable):
        """
        Receive the update from the Observable that the Observer class received.
        """
        pass

    def notify_observer(self, army_list):
        """
        Accepts the update from the update function in the Observer class.
        :return: Confirmation of the update.
        """
        # hobbit = army_list[0]
        # dwarf = army_list[1]
        # elf = army_list[2]
        # human = army_list[3]
        print(self.name, "is in Troop Command")
        print(self.name, "has been notified of the army count.\n")

    def defeated(self):
        """
        Calls the remove_observer function from the EyeOfSauron class.
        :return: Confirmation of the removal of the class from the observer list.
        """
        self.attached.remove_observer(self)
        print(self.name, "has been defeated.\n")
