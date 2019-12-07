"""
Builder Pattern example where a builder class builds a Pizza
"""

from enum import Enum


class BaseEnum(Enum):
    REGULAR = 0,
    WHOLEWHEAT = 1,
    CAULIFLOWER = 2


class ToppingEnum(Enum):
    RED_ONION = 0,
    PEPPERS = 1,
    SPINACH = 2,
    MUSHROOM = 3,
    PEPPERONI = 4,
    CHICKEN = 5,
    BACON = 6,
    BEYOND_MEAT = 7,
    PINEAPPLE = 8


class CheeseEnum(Enum):
    PARMESAN = 0,
    MOZZARELLA = 1,
    VEGAN_CHEESE = 2


class SauceEnum(Enum):
    TOMATO = 0,
    ALFREDO = 1,
    BBQ = 2



class Pizza():
    """
    As a contrived example let's look at a Pizza. as a complex object
    the pizza can have multiple toppins, cheeses, a base and even be
    "half and half" , that is have 2 pizza's in one or even be folded
    into a calzone.
    """

    def __init__(self) -> None:
        self.base = None
        self.sauce_1 = []
        self.sauce_2 = []
        self.toppings_1 = []
        self.toppings_2 = []
        self.cheeses_1 = []
        self.cheeses_2 = []
        self.is_calzone = None

    def __str__(self):
        toppings1_str = [str(topping) for topping in self.toppings_1]
        toppings2_str = [str(topping) for topping in self.toppings_2]
        cheeses1_str = [str(cheese) for cheese in self.cheeses_1]
        cheeses2_str = [str(cheese) for cheese in self.cheeses_2]

        toppings1 = ", ".join(toppings1_str)
        toppings2 = ", ".join(toppings2_str)
        cheeses_1 = ", ".join(cheeses1_str)
        cheeses_2 = ", ".join(cheeses2_str)
        return f"Pizza:\n" \
            f"------\n" \
            f"Calzone: {self.is_calzone}" \
            f"Base: {self.base}\n" \
            f"Sauce (1st Half): {self.sauce_1}\n" \
            f"Sauce (2nd Half): {self.sauce_2}\n" \
            f"Toppings (1st Half): {toppings1}\n" \
            f"Toppings (2nd Half): {toppings2}\n" \
            f"Cheeses (1st Half): {cheeses_1}\n" \
            f"Cheeses (2nd Half): {cheeses_2}\n"


class PizzaBuilder:

    def __init__(self):
        self._pizza = Pizza()

    def reset(self):
        self._pizza = Pizza()

    @property
    def pizza(self):
        completed_pizza = self._pizza
        self.reset()
        return completed_pizza

    def add_topping(self, topping: ToppingEnum, half_num: int = 0):
        if half_num == 0:
            self._pizza.toppings_1.append(topping)
            self._pizza.toppings_2.append(topping)
        elif half_num == 1:
            self._pizza.toppings_1.append(topping)
        elif half_num == 2:
            self._pizza.toppings_2.append(topping)
        else:
            raise Exception("Invalid half_num!")

    def add_cheese(self, cheese: CheeseEnum, half_num: int = 0):
        if half_num == 0:
            self._pizza.cheeses_1.append(cheese)
            self._pizza.cheeses_2.append(cheese)
        elif half_num == 1:
            self._pizza.cheeses_1.append(cheese)
        elif half_num == 2:
            self._pizza.cheeses_2.append(cheese)
        else:
            raise Exception("Invalid half_num!")

    def add_base(self, base: BaseEnum):
        self._pizza.base = base

    def add_sauce(self, sauce: SauceEnum, half_num: int = 0):
        if half_num == 0:
            self._pizza.sauce_1.append(sauce)
            self._pizza.sauce_2.append(sauce)
        elif half_num == 1:
            self._pizza.sauce_1.append(sauce)
        elif half_num == 2:
            self._pizza.sauce_2.append(sauce)
        else:
            raise Exception("Invalid half_num!")

    def make_calzone(self):
        self._pizza.is_calzone = True


class Menu:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """
    def __init__(self) -> None:
        self.builder = PizzaBuilder()
    """
    The Director can construct several product variations using the same
    building steps.
    """
    def prepare_cheese_pizza(self, half_num:int = 0) -> None:
        self.builder.add_base(BaseEnum.REGULAR)
        self.builder.add_sauce(SauceEnum.TOMATO, half_num)
        self.builder.add_cheese(CheeseEnum.MOZZARELLA, half_num)
        self.builder.add_cheese(CheeseEnum.MOZZARELLA, half_num)
        self.builder.add_cheese(CheeseEnum.PARMESAN, half_num)
        self.builder.add_cheese(CheeseEnum.PARMESAN, half_num)

    def prepare_pepperoni_pizza(self, half_num:int = 0) -> None:
        self.builder.add_base(BaseEnum.REGULAR)
        self.builder.add_sauce(SauceEnum.TOMATO, half_num)
        self.builder.add_cheese(CheeseEnum.MOZZARELLA, half_num)
        self.builder.add_topping(ToppingEnum.PEPPERONI, half_num)

    def prepare_vegan_pizza(self, half_num:int = 0) -> None:
        self.builder.add__base(BaseEnum.CAULIFLOWER)
        self.builder.add_sauce(SauceEnum.TOMATO, half_num)
        self.builder.add_cheese(CheeseEnum.VEGAN_CHEESE, half_num)
        self.builder.add_topping(ToppingEnum.BEYOND_MEAT, half_num)
        self.builder.add_topping(ToppingEnum.SPINACH, half_num)
        self.builder.add_topping(ToppingEnum.RED_ONION, half_num)
        self.builder.add_topping(ToppingEnum.PEPPERS, half_num)

    def order_half_half_pizza(self, pizza_order1, pizza_order2) -> Pizza:
        pizza_order1(1)
        pizza_order2(2)
        return self.builder.pizza

    def order_single_pizza(self, pizza_order):
        pizza_order()
        return self.builder.pizza


def main():
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    builder = PizzaBuilder()
    builder.add_base(BaseEnum.CAULIFLOWER)
    builder.make_calzone()
    builder.add_sauce(SauceEnum.ALFREDO, 1)
    builder.add_sauce(SauceEnum.BBQ)
    builder.add_cheese(CheeseEnum.MOZZARELLA, 0)
    builder.add_cheese(CheeseEnum.VEGAN_CHEESE)
    builder.add_topping(ToppingEnum.PINEAPPLE)
    builder.add_topping(ToppingEnum.SPINACH)
    builder.add_topping(ToppingEnum.BEYOND_MEAT, 2)
    pizza = builder.pizza
    print(pizza)


    menu = Menu()
    pizza = menu.order_half_half_pizza(menu.prepare_cheese_pizza,
                                       menu.prepare_pepperoni_pizza)
    print(pizza)


if __name__ == "__main__":
    main()
