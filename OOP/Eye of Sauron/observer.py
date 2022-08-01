from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Declares the update method used by the Observable.
    Credit https://www.c-sharpcorner.com/article/observer-design-pattern-exaple-with-python-sample/
    Credit https://en.proft.me/2017/02/21/observer-pattern-java-and-python/
    """
    def __init__(self, observable, observer_name):
        """
        Adds the class to the list of observers in the Observable class.
        """
        observable.add_observer(self)
        self.attached = observable
        self.name = observer_name

    @abstractmethod
    def update(self, observable):
        """
        Receive an update from the Observable.
        """
        pass
