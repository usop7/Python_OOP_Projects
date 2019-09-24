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

    def give_menu(self):
        options = [self.check_status, self.feed, self.give_medicine, self.play_games]
        question = "\n>> What would you like to do?\n" \
                   "(1) Check the status of your tamagotchi\n" \
                   "(2) Feed your tamagotchi\n" \
                   "(3) Give your tamagotchi a medicine\n" \
                   "(4) Play with your tamagotchi\n" \
                   "Please Select (1-3): "
        answer = int(input(question))
        options[answer-1]()

    def check_status(self):
        """Adjust status and print out relavant messages based on new status."""
        t = self._tamagotchi
        # Adjust status and print the updated status.
        diff = (datetime.now() - t.last_checked_time).seconds
        t.status.adjust_status(t.adjust_rate, diff)
        t.last_checked_time = datetime.now()
        print(t.status)

        # If health meter became 0, it dies.
        if t.status.health <= 0:
            t.die()
            print(f">> Your {t.name} died of sickness... RIP...")
            return
        # If health meter is lower than a certain meter, it gets sick.
        elif t.status.health < t.satisfactory_meter.health:
            t.got_sick()
            print(f"[{t.name}] I'm feeling sick. Please give me some medicine.")
        # If hunger meter hits 100, health adjustment rate becomes double.
        elif t.status.hunger >= 100:
            t.adjust_rate.health *= 2
            print("I'm super hangry!! I need food!")
        else:
            print(f"[{t.name}] Thanks for taking care of me, master!")

    def feed(self):
        """
        Give food options to choose and feed a tamagotchi.
        This will decrease the hunger level by the selected food calorie over Tamagotchi's health adjustment rate.
        If the selected food is tamagotchi's favorite food, decrease the hunger meter 10% more.
        """
        t = self._tamagotchi
        food_controller = FoodController()
        food = food_controller.give_food_option()
        if FoodController.is_fav_food(food, t.fav_food):
            decrement = t.status.decrease_hunger(food.calorie * 1.1 / t.adjust_rate.health)
            print(f"[{t.name}] {food.name} is my favorite food! Thank you, master!!")
        else:
            decrement = t.status.decrease_hunger(food.calorie / t.adjust_rate.health)
            print(f"[{t.name}] Thanks for the {food.name}!")
        print(f">> Hunger meter decreased by {round(decrement, 0)}!")

    def give_medicine(self):
        """
        If a tamagotchi is not sick, notify that it's not sick.
        If a tamagotchi is sick, make it recovered and print out thank msg.
        """
        t = self._tamagotchi
        if not t.is_sick():
            print(f"[{t.name}] I'm not sick. I don't need a medicine.")
        else:
            t.recover()
            print(f"[{t.name}] Thanks for the medicine. I feel better now.")

    def play_games(self):
        """Give game options to play, and fill up the happiness level by tamagotchi's happiness rate."""
        t = self._tamagotchi
        game_controller = GameController()
        game = game_controller.give_game_option()
        print(f"[{t.name}] {game.output}")
        increment = t.status.increase_happiness(game.level_of_fun / t.adjust_rate.happiness)
        print(f">> Happiness meter increased by {round(increment, 0)}!")
