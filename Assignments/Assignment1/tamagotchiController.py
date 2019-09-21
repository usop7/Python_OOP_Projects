import random
from tamagotchi import Boo
from tamagotchi import Frieza
from tamagotchi import Cell
from datetime import datetime


class TamagotchiCreator:

    @staticmethod
    def hatch():
        types = [Boo, Frieza, Cell]
        name = input("Please give a name to your tamagotchi: ")
        rand_int = random.randint(0, 2)
        tamagotchi = types[rand_int](name)
        print(f"Tamagotchi has been successfully hatched!\n{tamagotchi}")
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
        question = "\nWhat would you like to do?\n" \
                   "(1) Check Status\n" \
                   "Please Select (1-3): "
        answer = int(input(question))
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
