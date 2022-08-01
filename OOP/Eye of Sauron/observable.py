from abc import ABC, abstractmethod


class Observable(ABC):
    """
    Declares a set of methods for managing observers.
    Credit https://www.c-sharpcorner.com/article/observer-design-pattern-exaple-with-python-sample/
    Credit https://en.proft.me/2017/02/21/observer-pattern-java-and-python/
    """
    def __init__(self):
        """
        Initializes an empty list of observers.
        """
        self.observers_list = []

    def add_observer(self, observer):
        """
        Add an observer to the observer list.
        """
        pass

    @abstractmethod
    def remove_observer(self, observer):
        """
        Remove an observer from the observer list.
        """
        pass

    @abstractmethod
    def notify_observer(self, observer):
        """
        Notify all observers in the observer list of an event.
        """
        pass

    @abstractmethod
    def set_changed(self, observer):
        """
        Track whether or not the observable has changed.
        """
        pass

    @abstractmethod
    def has_changed(self, observer):
        """
        Mark that a change has been made to the observable.
        """
        pass

    @abstractmethod
    def clear_changed(self, observer):
        """
        Clear all changes made to the observable.
        """
        pass
