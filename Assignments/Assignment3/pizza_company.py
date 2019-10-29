import abc

class Pizza(abc.ABC):
    """
    The Data Source interface that all concrete Pizzas and
    decorators must adhere to. This interface defines add price method.
    """

    @abc.abstractmethod
    def print_ingredients(self, name, price):
        pass


class SignatureCrust(Pizza):
    """This class represents a Signature Crust pizza which is the
    base pizza of every pizza."""
    def __init__(self, price):
        self._price = price

    def print_ingredients(self, name, price):
        self._price += price
        return f"Signature Crust: 4.99\nTotal: {self._price}"


class SignatureCrustDecorator(Pizza):
    def __init__(self, base_pizza):
        self._base_pizza = base_pizza

    def print_ingredients(self, name, price):
        return self._base_pizza.print_ingredients(name, price)


class ParmigianoReggiano(SignatureCrustDecorator):
    """This is a decorator that adds a Parmigiano Reggiano topping
    on the base pizza."""

    def print_ingredients(self, name, price):
        return f"{name}: {price}\n{super().print_ingredients(name, price)}"


def main():
    base_pizza = SignatureCrust(4.99)

    parmigiano = input("yes?")

    if parmigiano == 'y':
        pizza = ParmigianoReggiano(base_pizza)

    print(pizza.print_ingredients('cheese', 3.99))


if __name__ == '__main__':
    main()



