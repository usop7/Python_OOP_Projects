import random
from tamagotchiType import TamagotchiType
from tamagotchi import Boo
from tamagotchi import Frieza
from tamagotchi import Cell
from datetime import datetime


class TamagotchiCreator:

    @staticmethod
    def hatch():
        name = input("\nPlease give a name to your tamagotchi: ")
        rand_int = random.randint(0, 2)
        if rand_int == 0:
            tamagotchi = Boo(name)
        elif rand_int == 1:
            tamagotchi = Frieza(name)
        else:
            tamagotchi = Cell(name)
        print(f"{tamagotchi.type_} {name} has been successfully hatched!")
        return tamagotchi


class TamagotchiManager:
    """Tamagotchi Manager holds methods that are used to manage a tamagotchi."""

    def __init__(self, tamagotchi):
        """
        Initialize a tamagotchi manager.
        :param tamagotchi: a tamagotchi object.
        """
        self._tamagotchi = tamagotchi

    def give_menu(self):
        options = [self.check_status]
        answer = int(input("(1) Check status\n"
                           "Please Select: "))
        options[answer-1]()

    def print_status(self):
        print(f"Current Status:\n{self._tamagotchi.status}")

    def check_status(self):
        """Adjust status and print out relavant messages based on new status."""
        t = self._tamagotchi
        diff = (datetime.now() - t.last_checked_time).seconds
        t.status.adjust_status(t.adjust_rate, diff)
        t.last_checked_time = datetime.now()
        print(t.status)
