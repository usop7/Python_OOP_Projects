"""
This module holds the controller that is responsible to create and
proceed a pizza order with users, and Pizza related classes and
decorators.
"""

import abc
from input_handler import NoCheeseAddedException
from ingredients import SignatureCrust
from ingredients import CheeseMenu
from ingredients import ToppingMenu


class OrderController:
    """This class represents a Pizza Order, and is responsible to prompt
    users with a Pizza Menu, Pizza check out option, etc."""

    def __init__(self):
        self._pizza = None

    def add_signature_crust(self):
        """Add a SignatureCrust to its pizza."""
        signature_crust = SignatureCrust()
        self._pizza = CrustPizza(signature_crust)
        self._pizza = BasePizzaDecorator(self._pizza, signature_crust)

    def add_cheese(self):
        """
        Keep prompting users with a cheese menu until they select 'Next'.
        Wrap a base pizza with a CheeseDecorator with a selected cheese,
        and print the ingredients that are added so far each time.

        If there is no cheese selected, an exception will be raised.
        """
        cheese = not None
        while cheese is not None:
            cheese = CheeseMenu.select_cheese()
            if cheese is not None:
                self._pizza = CheeseDecorator(self._pizza, cheese)
                print(f"\nYou've ordered:\n{self._pizza}")
            if not isinstance(self._pizza, CheeseDecorator):
                raise NoCheeseAddedException

    def add_topping(self):
        done = False
        while not done:
            topping = ToppingMenu.select_topping()
            if topping is not None:
                self._pizza = ToppingDecorator(self._pizza, topping)
                print(f"\nYou've ordered:\n{self._pizza}")
            else:
                done = True

    def start_order(self):
        """
        1. Add a Signature Crust to a pizza.
        2. Add cheeses.
        3. Add toppings.
        4. Checkout and complete the order.
        """

        # add a signature crust by default
        self.add_signature_crust()

        # add cheeses
        passed = False
        while not passed:
            try:
                self.add_cheese()
            except NoCheeseAddedException as e:
                print(f"{e}")
            else:
                passed = True

        # add toppings
        self.add_topping()

        # check out
        self.check_out()

    def check_out(self):
        """
        Print a well formatted bill that includes all pizza ingredients
        and the total price.
        """
        print(f"\n{'-'*30}\nHere is your bill.\n")
        print(f"{self._pizza}\n{'-'*30}\n"
              f"{self._pizza.total_price}")


class Pizza(abc.ABC):
    """
    The Data Source interface that all concrete Pizzas and
    decorators must adhere to. This interface defines add price method.
    """

    @abc.abstractmethod
    def add_price(self, price):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass

    @property
    @abc.abstractmethod
    def get_total_price(self):
        pass


class CrustPizza(Pizza):
    """A Crust Pizza is a Concrete Pizza that has a crust ingredient
    added on the pizza."""

    def __init__(self, crust):
        self._ingredient = crust
        self._total_price = 0

    def add_price(self, price):
        self._total_price += price

    def get_total_price(self):
        return f"Total Price: $ {self._total_price}"

    total_price = property(get_total_price)

    def __str__(self):
        return f"{self._ingredient.name}: $ {self._ingredient.price}"


class BasePizzaDecorator(Pizza):
    """This is a base decorator. This is a wrapper around
    a concrete pizza such as SignatureCrustPizza.
    All other decorators inherit from this class."""

    def __init__(self, base_pizza, ingredient):
        """
        Initialize a BasePizzaDecorator with a base pizza and a new
        ingredient, and add the ingredient's price.
        :param base_pizza: Pizza
        :param ingredient: Ingredient objects such as cheese, toppings
        """
        self._base_pizza = base_pizza
        self._ingredient = ingredient
        self.add_price(ingredient.price)

    def add_price(self, price):
        self._base_pizza.add_price(price)

    def get_total_price(self):
        return self._base_pizza.get_total_price()

    total_price = property(get_total_price)

    def __str__(self):
        return f"{self._ingredient}"


class CheeseDecorator(BasePizzaDecorator):
    """This is a decorator that adds a cheese ingredient to a
    base pizza. This decorator can wrap around a concrete Pizza or
    another Decorator."""

    def __str__(self):
        """
        Return a formatted string of its base pizza's ingredients and
        its ingredient.
        :return: Sring
        """
        return f"{self._base_pizza.__str__()}\n{self._ingredient}"


class ToppingDecorator(BasePizzaDecorator):
    """This is a decorator that adds a topping ingredient to a
    base pizza. This decorator can wrap around a concrete Pizza or
    another Decorator."""

    def __str__(self):
        return f"{self._base_pizza.__str__()}\n{self._ingredient}"


def main():
    """Instantiate an Order Controller and start an order."""

    order_controller = OrderController()
    order_controller.start_order()


if __name__ == '__main__':
    main()
