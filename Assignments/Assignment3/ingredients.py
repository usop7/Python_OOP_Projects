from enum import Enum
from input_handler import InputHandler


class SignatureCrust:
    def __init__(self):
        self.name = "Signature Crust"
        self.price = 4.99

    def __str__(self):
        return f"{self.name}: $ {self.price}"


class Cheese:
    """This class represents a cheese."""

    def __init__(self, name, price):
        """
        Initialize a cheese item.
        :param type_: a String
        :param price: a float
        """
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: $ {self.price}"


class CheeseMenu:
    """This class embodies a list of cheese and a methods that give a
    cheese menu option to users."""

    cheese_list = [
        Cheese("Parmigiano Reggiano", 4.99),
        Cheese("Fresh Mozzarella", 3.99),
        Cheese("Vegan Cheese", 5.99)
    ]

    @staticmethod
    def select_cheese():
        """
        Prompt user with cheese list, and return the selected cheese.
        :return: Cheese object
        """
        question = f"\nStep 1: Select your cheese!\n{'-'*40}\n"
        i = 1
        for cheese in CheeseMenu.cheese_list:
            question += f"{i}. {cheese}\n"
            i += 1
        question += f"{i}. Next\n{'-'*40}\nPlease select: "
        return InputHandler.prompt_menu(question, CheeseMenu.cheese_list)


class Topping:
    """This class represents a topping."""

    def __init__(self, name, price):
        """
        Initialize a topping item.
        :param name: a String
        :param price: a float
        """
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: $ {self.price}"


class ToppingMenu:
    """This class embodies a list of topping and a methods that give a
    topping menu option to users."""

    topping_list = [
        Topping("Peppers", 1.5),
        Topping("Pineapple", 2),
        Topping("Mushrooms", 1.5),
        Topping("Fresh Basil", 2),
        Topping("Spinach", 1),
        Topping("Pepperoni", 3),
        Topping("Beyond Meat", 4)
    ]

    @staticmethod
    def select_topping():
        """
        Prompt user with a topping list, and return the selected topping.
        :return: None or Topping object
        """
        question = f"\nStep 2: Select your topping!\n{'-'*40}\n"
        i = 1
        for topping in ToppingMenu.topping_list:
            question += f"{i}. {topping}\n"
            i += 1
        question += f"{i}. Check Out\n{'-'*40}\nPlease select: "
        return InputHandler.prompt_menu(question, ToppingMenu.topping_list)
