import abc
from ingredients import CheeseMenu
from ingredients import ToppingMenu


class Pizza(abc.ABC):
    """
    The Data Source interface that all concrete Pizzas and
    decorators must adhere to. This interface defines add price method.
    """

    @abc.abstractmethod
    def __str__(self):
        pass


class SignatureCrust(Pizza):
    """This class represents a Signature Crust pizza which is the
    base pizza of every pizza."""

    def __str__(self):
        return f"Signature Crust: $ 4.99"


class BasePizzaDecorator(Pizza):
    def __init__(self, base_pizza):
        self.base_pizza = base_pizza

    def add(self):
        self.base_pizza.add()

    def __str__(self):
        return self.base_pizza.__str__()


class ParmigianoReggiano(BasePizzaDecorator):
    """This is a decorator that adds a Parmigiano Reggiano topping
    on the base pizza."""

    def __str__(self):
        return f"{super().__str__()}\n" \
               f"Parmigiano Reggiano: $ 4.99"


def main():
    base_pizza = SignatureCrust()
    pizza = BasePizzaDecorator(base_pizza)

    cheese = 1
    while cheese is not None:
        cheese_menu = CheeseMenu()
        cheese = cheese_menu.select_cheese()
        pizza = ParmigianoReggiano(pizza)


    print(pizza)



if __name__ == '__main__':
    main()



