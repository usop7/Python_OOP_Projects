from tamagotchiController import TamagotchiCreator
from tamagotchiController import TamagotchiManager


class Console:
    """This class embodies the basic functions and attributes of a game console."""

    def __init__(self):
        self.manager = None

    def start_game(self):
        """
        If there is no tamagotchi, ask user if they want to hatch one, and call Tamagotchi Creator.
        If there is a tamagotchi, call TamagotchiManager and call give menu method.
        """
        while True:
            if self.manager is None or self.manager.is_tamagotchi_alive() is False:
                answer = input("\n>> No tamagotchi exists. Do you want to hatch one? (Y/N): ")
                if answer.lower() == "y":
                    self.manager = TamagotchiManager(TamagotchiCreator.hatch())
            else:
                self.manager.give_menu()


def main():
    """
    Creates a controller and simulates the asteroids' movements.
    """
    console = Console()
    console.start_game()


if __name__ == "__main__":
    main()
