from tamagotchiController import TamagotchiCreator
from tamagotchiController import TamagotchiManager


class Console:
    """This class embodies the basic functions and attributes of a game console."""

    def __init__(self):
        self._tamagotchi = None

    def start_game(self):
        """
        If there is no tamagotchi, ask user if they want to hatch one, and call Tamagotchi Creator.
        If there is a tamagotchi, call TamagotchiManager and call give menu method.
        """
        while True:
            if self._tamagotchi is None or self._tamagotchi.is_alive() is False:
                answer = input(">> No tamagotchi exists. Do you want to hatch one? (Y/N): ")
                if answer.lower() == "y":
                    self._tamagotchi = TamagotchiCreator.hatch()
            else:
                manager = TamagotchiManager(self._tamagotchi)
                manager.give_menu()


def main():
    """
    Creates a controller and simulates the asteroids' movements.
    """
    console = Console()
    console.start_game()


if __name__ == "__main__":
    main()
