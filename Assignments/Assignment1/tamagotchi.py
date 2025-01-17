"""
All code related to a tamagotchi and types of tamagotchi belong to this module.
"""
from datetime import datetime
from status import Status
from enum import Enum
import abc


class TamagotchiType(Enum):
    BOO = "Boo"
    FRIEZA = "Frieza"
    CELL = "Cell"


class Tamagotchi(abc.ABC):
    """
    This class serves as a base class and should be inherited from
    a specific tamagotchi type class.
    """

    def __init__(self, name):
        """
        Initialize a Tamagotchi.
        """
        self._name = name
        self._birth_time = datetime.now()
        self._last_checked_time = datetime.now()
        self._status = Status(Status.max_meter, Status.max_meter, Status.min_meter)  # Health, Happiness, Hunger
        self._type_ = TamagotchiType.BOO
        # Represents adjustment rate per second for each status meter (health, happiness, hunger)
        self.adjust_rate = None
        # Represents minimum/maximum meters required for each status to satisfy a Boo
        self.satisfactory_meter = None
        # favorite food list
        self.fav_food = []
        self._is_alive = True
        self._is_sick = False

    def get_name(self):
        """:return: a String, name"""
        return self._name

    name = property(get_name)

    def is_alive(self):
        """:return: boolean, True if it's alive."""
        return self._is_alive

    def die(self):
        """Sets is alive to False."""
        self._is_alive = False

    def is_sick(self):
        """:return: boolean, True if it's sick."""
        return self._is_sick

    def recover(self):
        """Sets is sick to False, and fill up the health meter to 100."""
        self._is_sick = False
        self.status.health = 100

    def got_sick(self):
        """Sets is sick to True."""
        self._is_sick = True

    def get_last_checked_time(self):
        """:return: a datetime, last checked time"""
        return self._last_checked_time

    def set_last_checked_time(self, checked_time):
        """Sets last checked time.
        :param checked_time: a datetime"""
        self._last_checked_time = checked_time

    def get_status(self):
        """Returns tamagotchi's current status.
        :return: Status object"""
        return self._status

    status = property(get_status)
    last_checked_time = property(get_last_checked_time, set_last_checked_time)

    def __str__(self):
        return f"Name: {self._name}\n" \
               f"Type: {self._type_.value}\n" \
               f"Birthday: {self._birth_time}\n" \
               f"Current Status\n{self._status}\n"


class Boo(Tamagotchi):
    """This class embodies the methods and attributes of a boo."""

    def __init__(self, name):
        """
        Initialize a Boo.
        """
        super().__init__(name)
        self._type_ = TamagotchiType.BOO
        self.adjust_rate = Status(1, 1, 1)
        self.satisfactory_meter = Status(40, 60, 50)
        self.fav_food = ["Chocolate", "Beer", "Church's chicken"]


class Frieza(Tamagotchi):
    """This class embodies the methods and attributes of a boo."""

    def __init__(self, name):
        """
        Initialize a Frieza.
        """
        super().__init__(name)
        self._type_ = TamagotchiType.FRIEZA
        self.adjust_rate = Status(0.5, 0.5, 0.5)
        self.satisfactory_meter = Status(50, 50, 50)
        self.fav_food = ["Church's chicken", "Steak", "Shrimp"]


class Cell(Tamagotchi):
    """This class embodies the methods and attributes of a boo."""

    def __init__(self, name):
        """
        Initialize a Cell.
        """
        super().__init__(name)
        self._type_ = TamagotchiType.CELL
        self.adjust_rate = Status(0.3, 0.4, 0.5)
        self.satisfactory_meter = Status(50, 50, 50)
        self.fav_food = ["Android 17", "Android 18"]
