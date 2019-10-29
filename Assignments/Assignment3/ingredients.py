from input_handler import InputHandler
from input_handler import CommandNotFoundException

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
        return f"{self.name} ({self.price} calorie)"


class CheeseMenu:
    """This class embodies a list of food and food related methods."""

    def __init__(self):
        """
        Initialize a food  controller.
        """
        self._cheese_list = [
            Cheese("Parmigiano Reggiano", 4.99),
            Cheese("Fresh Mozzarella", 3.99),
            Cheese("Vegan Cheese", 5.99)
        ]

    def give_cheese_option(self):
        """
        Prompt user with cheese list, and return the selected cheese.
        :return: Cheese object
        """
        question = "\nSelect your cheese!\n" \
                   "----------------------------------\n"
        i = 1
        for cheese in self._cheese_list:
            question += f"{i}: {cheese}\n"
            i += 1
        question += "4: Skip\n" \
                    "----------------------------------\n" \
                    "Please select: "

        while True:
            answer = input(question)
            if answer == str(len(self._cheese_list) + 1):
                return None
            else:
                try:
                    InputHandler.validate(len(self._cheese_list)+1, answer)
                except ValueError:
                    print("\n[Error] Please type an integer!")
                except CommandNotFoundException as e:
                    print(f"{e}")
                else:
                    return self._cheese_list[int(answer) - 1]
