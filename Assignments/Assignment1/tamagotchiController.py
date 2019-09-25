import random
from datetime import datetime
from tamagotchi import Boo
from tamagotchi import Frieza
from tamagotchi import Cell
from food import FoodController
from gameController import GameController


class TamagotchiCreator:
    """Tamagotchi Creator holds a method to create a random type of tamagotchi."""

    @staticmethod
    def hatch():
        """
        Selects a tamagotchi type randomly and creates the selected type of tamagotchi and return it.
        :return: Tamagotchi
        """
        types = [Boo, Frieza, Cell]
        name = input(">> Please give a name to your tamagotchi: ")
        rand_int = random.randint(0, 2)
        tamagotchi = types[rand_int](name)
        print(f">> Tamagotchi has been successfully hatched!\n{tamagotchi}")
        return tamagotchi


class TamagotchiManager:
    """Tamagotchi Manager holds methods that are used to manage a tamagotchi."""

    def __init__(self, tamagotchi):
        """
        Initialize a tamagotchi manager.
        :param tamagotchi: a tamagotchi object.
        """
        self._tamagotchi = tamagotchi

    def get_tamagotchi(self):
        return self._tamagotchi

    tamagotchi = property(get_tamagotchi)

    def is_tamagotchi_alive(self):
        """Returns true if a tamagotchi is alive."""
        return self._tamagotchi.is_alive()

    def give_menu(self):
        """Prompts user with a menu list, and call the selected method."""
        options = [self.check_status, self.feed, self.give_medicine, self.play_games]

        # Create a list of valid answers
        valid_answers = []
        i = 0
        while i <= len(options):
            valid_answers.append(str(i))
            i += 1

        # Repeat until the user enters the valid options (1-4)
        answer = 0
        while answer not in valid_answers:
            answer = input("What would you like to do?\n"
                           "(1) Check the status of your tamagotchi \n"
                           "(2) Feed your tamagotchi\n"
                           "(3) Give your tamagotchi a medicine\n"
                           "(4) Play with your tamagotchi\n"
                           "Please select(1-4): \n")
        answer = int(answer)
        options[answer-1]()

    def update_last_checked_time(self):
        """Updates a tamagotchi's last checked to time to the current time."""
        self._tamagotchi.last_checked_time = datetime.now()

    def update_status(self):
        """Updates the status based on tamagotchi's adjustment rates and the time difference
        between the current time and the last checked time.
        If a tamagotchi died, notify user and redirect user to the console."""
        t = self._tamagotchi
        time_diff = (datetime.now() - t.last_checked_time).seconds
        t.status.adjust_status(self._tamagotchi.adjust_rate, time_diff)
        self.update_last_checked_time()
        # If health meter became 0, it dies, and redirect user to the console.
        if t.status.health <= 0:
            t.die()
            print(f">> Your {t.name} died of sickness... RIP...")
            return

    def check_status(self):
        """Updates Status of a tamagotchi and adjusts relevant attributes based on the new status."""

        t = self._tamagotchi
        self.update_status()
        if self.is_tamagotchi_alive():
            print(t.status)
            # If health meter is lower than a certain meter, it gets sick.
            if t.status.health < t.satisfactory_meter.health:
                t.got_sick()
                print(f"[{t.name}] I'm feeling sick. Please give me some medicine.")
            # If hunger meter hits 100, health adjustment rate becomes double.
            elif t.status.hunger >= 100:
                t.adjust_rate.health *= 2
                print("I'm super hangry!! I need food!")
            # If everything is fine, print out thank you message.
            else:
                print(f"[{t.name}] Thanks for taking care of me, master!")

    def feed(self):
        """
        Give food options to choose and feed a tamagotchi.
        This will decrease the hunger level by the selected food calorie over Tamagotchi's health adjustment rate.
        If the selected food is tamagotchi's favorite food, decrease the hunger meter 10% more.
        """
        t = self._tamagotchi
        self.update_status()
        if self.is_tamagotchi_alive():
            # Prompt user with food options
            food_controller = FoodController()
            food = food_controller.give_food_option()
            # If selected food is in a tamagotchi's favorite food list, hunger meter decreases by 110%.
            if FoodController.is_fav_food(food, t.fav_food):
                decrement = t.status.decrease_hunger(food.calorie * 1.1 / t.adjust_rate.health)
                print(f"[{t.name}] {food.name} is my favorite food! Thank you, master!!")
            else:
                decrement = t.status.decrease_hunger(food.calorie / t.adjust_rate.health)
                print(f"[{t.name}] Thanks for the {food.name}!")
            # Prints how much hunger meter was decreased, and the updated status.
            print(f">> Hunger meter decreased by {round(decrement, 0)}!\n{t.status}")

    def give_medicine(self):
        """
        If a tamagotchi is not sick, notify that it's not sick.
        If a tamagotchi is sick, recover it and print out thank you message.
        """
        t = self._tamagotchi
        self.update_status()
        if self.is_tamagotchi_alive():
            if not t.is_sick():
                print(f"[{t.name}] I'm not sick. I don't need a medicine.\n{t.status}")
            else:
                t.recover()
                print(f"[{t.name}] Thanks for the medicine. I feel better now.\n{t.status}")

    def play_games(self):
        """Give game options to play, and fill up the happiness level by tamagotchi's happiness rate."""
        t = self._tamagotchi
        self.update_status()
        if self.is_tamagotchi_alive():
            # Game Controller prompts user with a mini game list.
            game_controller = GameController()
            game = game_controller.give_game_option()
            # Print out the selected game's output, and adjust happiness level based on its level of fun.
            print(f"[{t.name}] {game.output}")
            increment = t.status.increase_happiness(game.level_of_fun / t.adjust_rate.happiness)
            print(f">> Happiness meter increased by {round(increment, 0)}!\n{t.status}")
