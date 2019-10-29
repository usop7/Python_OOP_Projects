from input_handler import InputHandler


class Cheese:
    """This class represents a cheese."""

    def __init__(self, name, price):
        """
        Initialize a cheese item.
        :param name: a String
        :param price: a float
        """
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (${self.price})"


class CheeseMenu:
    """This class embodies a list of cheese and a methods that give a
    cheese menu option to users."""

    def __init__(self):
        """Initialize a cheese menu with a list of cheese."""
        self._cheese_list = [
            Cheese("Parmigiano Reggiano", 4.99),
            Cheese("Fresh Mozzarella", 3.99),
            Cheese("Vegan Cheese", 5.99)
        ]

    def select_cheese(self):
        """
        Prompt user with cheese list, and return the selected cheese.
        :return: Cheese object
        """
        question = f"\nSelect your cheese!\n{'-'*40}\n"
        i = 1
        for cheese in self._cheese_list:
            question += f"{i}: {cheese}\n"
            i += 1
        question += f"{i}: Skip\n{'-'*40}\nPlease select: "
        return InputHandler.prompt_menu(question, self._cheese_list)


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
        return f"{self.name} (${self.price})"


class ToppingMenu:
    """This class embodies a list of topping and a methods that give a
    topping menu option to users."""

    def __init__(self):
        """Initialize a topping menu with a list of toppings."""
        self._topping_list = [
            Topping("Peppers", 1.5),
            Topping("Pineapple", 2),
            Topping("Mushrooms", 1.5),
            Topping("Fresh Basil", 2),
            Topping("Spinach", 1),
            Topping("Pepperoni", 3),
            Topping("Beyond Meat", 4)
        ]

    def select_topping(self):
        """
        Prompt user with a topping list, and return the selected topping.
        :return: None or Topping object
        """
        question = f"\nSelect your topping!\n{'-'*40}\n"
        i = 1
        for topping in self._topping_list:
            question += f"{i}: {topping}\n"
            i += 1
        question += f"{i}: Skip\n{'-'*40}\nPlease select: "
        return InputHandler.prompt_menu(question, self._topping_list)
