import abc
from input_handler import NoCheeseAddedException
from ingredients import SignatureCrust
from ingredients import CheeseMenu
from ingredients import ToppingMenu
from ingredients import CheeseType
from ingredients import ToppingType


class OrderController:
    """This class represents a Pizza Order, and is responsible to prompt
    users with a Pizza Menu, Pizza check out option, etc."""

    def __init__(self):
        self._pizza = None

    def add_signature_crust(self):
        """Add a SignatureCrust to its pizza."""
        crust = SignatureCrust()
        self._pizza = SignatureCrustPizza(crust)
        self._pizza = BasePizzaDecorator(self._pizza, crust)

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
                print(self._pizza)
            if not isinstance(self._pizza, CheeseDecorator):
                raise NoCheeseAddedException

    def check_out(self):
        """
        Print a well formatted bill that includes all pizza ingredients
        and the total price.
        """
        print(f"\n{'-'*40}\nHere is your bill.\n")
        print(f"{self._pizza}\n{self._pizza.total_price}")
        print(f"{'-'*40}")


class Pizza(abc.ABC):
    """
    The Data Source interface that all concrete Pizzas and
    decorators must adhere to. This interface defines add price method.
    """

    @abc.abstractmethod
    def add_ingredient(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass

    @property
    @abc.abstractmethod
    def get_total_price(self):
        pass


class SignatureCrustPizza(Pizza):
    """A Signature Crust Pizza is a Concrete Pizza that has a
    signature crust ingredient added on the pizza."""

    def __init__(self, ingredient):
        self._ingredient = ingredient
        self._total_price = 0

    def add_ingredient(self):
        self._total_price += self._ingredient.price

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
        ingredient.
        :param base_pizza: Pizza
        :param ingredient: Ingredient objects such as cheese, toppings
        """
        self._base_pizza = base_pizza
        self._ingredient = ingredient
        self.add_ingredient()

    def add_ingredient(self):
        self._base_pizza.add_ingredient()

    def get_total_price(self):
        return self._base_pizza.get_total_price()

    total_price = property(get_total_price)

    def __str__(self):
        return f"{self._ingredient}"


class CheeseDecorator(BasePizzaDecorator):
    """This is a decorator that adds a cheese ingredient to a
    base pizza. This decorator can wrap around a concrete Pizza or
    another Decorator."""

    def add_ingredient(self):
        self._base_pizza.add_ingredient()

    def __str__(self):
        return f"{self._base_pizza.__str__()}\n{self._ingredient}"


def main():
    order_controller = OrderController()

    # Add Signature Crust by default
    order_controller.add_signature_crust()

    # Call Cheese Menu
    passed = False
    while not passed:
        try:
            order_controller.add_cheese()
        except NoCheeseAddedException as e:
            print(f"{e}")
        else:
            passed = True

    order_controller.check_out()


if __name__ == '__main__':
    main()
