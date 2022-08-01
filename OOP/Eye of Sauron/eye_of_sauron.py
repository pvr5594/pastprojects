from observable import Observable


class EyeOfSauron(Observable):
    """
    Inherits from the Observable class and notifies observers in the observer list when there is an event.
    Credit https://www.c-sharpcorner.com/article/observer-design-pattern-exaple-with-python-sample/
    Credit https://en.proft.me/2017/02/21/observer-pattern-java-and-python/
    """
    def __init__(self):
        """
        Initializes the class with the observer list set as empty and variable counts set at 0
        """
        self.observer = []
        self.hobbit_count = 0
        self.dwarf_count = 0
        self.elf_count = 0
        self.human_count = 0

    def add_observer(self, observer):
        """
        Triggers the addition of an observer to the observer list.
        """
        self.observer.append(observer)

    def remove_observer(self, observer):
        """
        Triggers the removal of an observer from the observer list (Only triggers if the list is not empty).
        """
        if observer in self.observer:
            self.observer.remove(observer)

    def notify_observer(self, observer):
        """
        Triggers the notification of the observers in the observer list (Only triggers if the list is not empty).
        """
        for observer in self.observer:
            observer.notify_observer(self.observer)

    def set_changed(self, observer):
        """
        Triggers the tracking of a change made in the observable.
        """
        observer.set_changed(self.observer)

    def has_changed(self, observer):
        """
        Triggers the marking of a change made in the observable.
        """
        observer.has_changed(self.observer)

    def clear_changed(self, observer):
        """
        Triggers the clearing of all changes made in the observable.
        """
        observer.clear_changed(self.observer)

    def set_enemies(self, hobbit_count, dwarf_count, elf_count, human_count):
        """
        Sets the change, puts the changes into a list, and calls the notify_observer method to notify the observer of
        the change.
        :param hobbit_count: number of hobbits
        :param dwarf_count: number of dwarfs
        :param elf_count: number of elfs
        :param human_count: number of humans
        :return: Confirmation that the notification has been received.
        """
        self.hobbit_count = hobbit_count
        self.dwarf_count = dwarf_count
        self.elf_count = elf_count
        self.human_count = human_count
        army = [self.hobbit_count, self.dwarf_count, self.elf_count, self.human_count]
        self.notify_observer(army)
        print("Troop Command has confirmed reports that the advancing enemy force contains", {hobbit_count}, "hobbits,",
              {dwarf_count}, "dwarfs,", {elf_count}, "elfs, and", {human_count}, "humans.\n")
