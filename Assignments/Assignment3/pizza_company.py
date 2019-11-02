import abc
from ingredients import CheeseMenu
from ingredients import ToppingMenu
from ingredients import CheeseType
from ingredients import ToppingType


class OrderController:
    def __init__(self):
        self._pizza = SignaturePizzaDecorator(SignatureCrust())
        self._total_price = 0
        self._cheese_list = {
            CheeseType.PARMIGIANO: ParmigianoReggianoDecorator,
            CheeseType.MOZZARELLA: ParmigianoReggianoDecorator,
            CheeseType.VEGAN: ParmigianoReggianoDecorator
        }

    def add_cheese(self):
        cheese = 1
        while cheese is not None:
            cheese = CheeseMenu.select_cheese()
            if cheese is not None:
                self._pizza = self._cheese_list[cheese.type_](self._pizza)

    def check_out(self):
        print(self._pizza)


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


class SignaturePizzaDecorator(Pizza):
    def __init__(self, crust):
        self._crust = crust

    def __str__(self):
        return self._crust.__str__()


class ParmigianoReggianoDecorator(SignaturePizzaDecorator):
    """This is a decorator that adds a Parmigiano Reggiano topping
    on the base pizza."""

    def __str__(self):
        return f"{super().__str__()}\n" \
               f"Parmigiano Reggiano: $ 4.99"


def main():

    order_controller = OrderController()
    order_controller.add_cheese()
    order_controller.check_out()


if __name__ == '__main__':
    main()
