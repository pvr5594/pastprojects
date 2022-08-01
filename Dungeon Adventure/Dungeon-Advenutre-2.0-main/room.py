import random

from phonenix import Phoenix
from emu import Emu
from raven import Raven
from sphinx import Sphinx

from mock_game import MockGame as Game
from battleground import Battleground
from quiz import Quiz


class Room:
    def __init__(self, room_id, location):
        self.__diff = 1
        self.__monster = None
        self.__phoenix = Phoenix
        self.__emu = Emu
        self.__emu = False
        self.__raven = Raven
        self.__raven = False
        if random.random() < 0.06:
            self.__emu = True
        elif random.random() < 0.06:
            self.__raven = True

        self.__health_p = False
        if random.random() < 0.1:
            self.__health_p = True
        self.__vision_p = False
        if random.random() < 0.1:
            self.__vision_p = True
        self.__pit = False
        if random.random() < 0.1:
            self.__pit = random.randrange(1, 20)
        self.__exit = False
        self.__doors = {
            "n": None,
            "w": None,
            "e": None,
            "s": None
        }
        self.__has_player = False
        self.__pillar = False
        self.__room_id = room_id
        self.__location = location
        self.__quiz_type = None

    def get_id(self):
        """
        Returns id
        """
        return self.__room_id

    def get_location(self):
        """
        Returns location
        """
        return self.__location

    def __str__(self):
        """
        Builds 2D Graphical representation of the room
        """
        north = " " if self.__doors['n'] else "-"
        west = " " if self.__doors['w'] else "|"
        east = " " if self.__doors['e'] else "|"
        south = " " if self.__doors['s'] else "-"

        item = None

        if self.__has_player:
            item = "@"
        elif self.__pillar:
            item = self.__pillar
        elif self.__exit:
            item = "O"
        elif self.__health_p and self.__vision_p:
            item = "B"
        elif self.__pit:
            item = "X"
        elif self.__health_p:
            item = "H"
        elif self.__vision_p:
            item = "V"
        elif self.__emu:
            item = "!"
        elif self.__raven:
            item = "?"
        else:
            item = " "

        return f"+{north}+\n{west}{item}{east}\n+{south}+"

    def get_player(self):
        """
        Returns True is player present, False otherwise
        """
        return self.__has_player

    def link(self, room, dir):
        """
        Given a Room object, checks if the complimentary direction of that room
        is walled.  If so, walls this room in the given direction.  Otherwise, stores
        a pointer to that room in the given direction.
        """
        compliment = {
            "n": "s",
            "w": "e",
            "e": "w",
            "s": "n",
        }
        make_link = True
        if room.get_dir(compliment[dir]) is False:
            make_link = False
        if make_link:
            self.__doors[dir] = room
        else:
            self.__doors[dir] = False

    def get_dir(self, dir):
        """
        Returns the state of the connection in the indicated direction.
        """
        return self.__doors[dir]

    def is_exit(self):
        """
        Returns True if this is the exit, False otherwise
        """
        return self.__exit

    def set_pillar(self, pillar):
        """
        Adds the given pillar to the room if it's a valid pillar.
        """
        pillars = ["A", "E", "I", "P"]
        if pillar in pillars:
            self.__pillar = pillar

        if self.__pillar == "A":
            self.__quiz_type = 'Abstraction'
        elif self.__pillar == "E":
            self.__quiz_type = 'Encapsulation'
        elif self.__pillar == "I":
            self.__quiz_type = 'Inheritance'
        elif self.__pillar == "P":
            self.__quiz_type = 'Polymorphism'

    def get_pillar(self):
        """
        Returns the pillar, if any, stored in the room.  False otherwise.
        """
        return self.__pillar

    def quiz_type(self):
        return self.__quiz_type

    def clear_room(self):
        """
        Deletes all items from the room.
        """
        self.__health_p = False
        self.__pit = False
        self.__vision_p = False
        self.__raven = False
        self.__emu = False


    def set_as_exit(self):
        """
        Deletes all items from the room and then sets room as exit.
        """
        self.clear_room()
        self.__exit = True

    def leave(self):
        """
        Marks the room as no longer containing the player.
        """
        self.__has_player = False

    def wall(self, dir):
        """
        Sets the specified direction as a wall.
        """
        self.__doors[dir] = False

    def enter(self, war):
        """
        Called when the adventurer enters a room.  Calls the appropriate
        methods based on the room's contents, then sets the room as containing
        the player.
        """
        self.__game = Game

        if self.__exit:
            war.exit()
            self.__has_player = True
            return
        if self.__pillar:
            war.earn_pillar(self.__pillar)
            self.__pillar = False
            quiz = Quiz()
            self.__monster = Sphinx(self.__diff, "Sphinx", Game())
            quiz.start_quiz(self.__quiz_type, war, self.__monster)
        if self.__vision_p:
            war.add_vision_potion()
            self.__vision_p = False
        if self.__health_p:
            war.add_health_potion()
            self.__health_p = False
        if self.__pit:
            war.take_damage(self.__pit, "a pit trap")
        if self.__emu:
            self.__game.announce(Game(), f"The Hero {war} has found the EMU")
            self.__emu = False
            self.__monster = Emu(self.__diff, "Emu", Game())
            battleground = Battleground()
            battleground.combat(war, self.__monster)
        if self.__raven:
            self.__game.announce(Game(), f"The Hero {war} has found the RAVEN")
            self.__raven = False
            self.__monster = Raven(self.__diff, "Raven", Game())
            battleground = Battleground()
            battleground.combat(war, self.__monster)

        self.__has_player = True

