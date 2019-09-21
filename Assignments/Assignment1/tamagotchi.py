"""
All code related to a tamagotchi and types of tamagotchi belong to this module.
"""
from datetime import datetime
from status import Status
from tamagotchiType import TamagotchiType
from food import Food


class Tamagotchi:
    """
    A tamagotchi class that models a tamagotchi with a name,
    This class serves as a base class and should be inherited from
    a specific tamagotchi type class.
    """

    def __init__(self, name):
        """
        Initialize a Tamagotchi.
        :param name: a String
        """
        self._name = name
        self._birth_time = datetime.now()
        self._last_checked_time = datetime.now()
        self._status = Status(Status.max_meter, Status.max_meter, Status.min_meter)  # Health, Happiness, Hunger
        self._is_alive = True
        self._type_ = None

    def is_alive(self):
        """:return: boolean, True if it's alive."""
        return self._is_alive

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
        return f"-------------------------------\n" \
               f"Name: {self._name}\n" \
               f"Type: {self._type_.value}\n" \
               f"Birthday: {self._birth_time}\n" \
               f"Current Status\n{self._status}\n" \
               f"--------------------------------\n"


class Boo(Tamagotchi):
    """This class embodies the methods and attributes of a boo."""

    def __init__(self, name):
        """
        Initialize a Boo.
        """
        super().__init__(name)
        self._type_ = TamagotchiType.BOO
        # Represents adjustment rate per second for each status meter (health, happiness, hunger)
        self.adjust_rate = Status(1, 2, 5)
        # Represents minimum/maximum meters required for each status to satisfy a Boo
        self.satisfactory_meter = Status(40, 60, 50)
        # favorite food list
        self.fav_food = [
            Food("Chocolate", 5),
            Food("Beer", 1),
            Food("Church's chicken", 10)
        ]


class Frieza(Tamagotchi):
    """This class embodies the methods and attributes of a boo."""

    def __init__(self, name):
        """
        Initialize a Boo.
        """
        super().__init__(name)
        self._type_ = TamagotchiType.FRIEZA
        # Represents adjustment rate per second for each status meter (health, happiness, hunger)
        self.adjust_rate = Status(2, 3, 6)
        # Represents minimum/maximum meters required for each status to satisfy a Boo
        self.satisfactory_meter = Status(50, 50, 50)
        # favorite food list
        self.fav_food = [
            Food("Chocolate", 5),
            Food("Beer", 1),
            Food("Church's chicken", 10)
        ]


class Cell(Tamagotchi):
    """This class embodies the methods and attributes of a boo."""

    def __init__(self, name):
        """
        Initialize a Boo.
        """
        super().__init__(name)
        self._type_ = TamagotchiType.CELL
        # Represents adjustment rate per second for each status meter (health, happiness, hunger)
        self.adjust_rate = Status(2, 3, 6)
        # Represents minimum/maximum meters required for each status to satisfy a Boo
        self.satisfactory_meter = Status(50, 50, 50)
        # favorite food list
        self.fav_food = [
            Food("Chocolate", 5),
            Food("Beer", 1),
            Food("Church's chicken", 10)
        ]
