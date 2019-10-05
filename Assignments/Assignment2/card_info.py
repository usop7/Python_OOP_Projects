"""This module holds classes regarding card information."""

from enum import Enum
from input_handler import InputHandler
from input_handler import CommandNotFoundException


class CardType(Enum):
    ID = "ID Card"
    CREDIT = "Credit Card"
    GIFT = "Gift Card"
    MEMBERSHIP = "Membership Card"
    LOYALTY = "Loyalty Card"
    BUSINESS = "Business Card"
    OTHER = "Other Types of Card"

    @staticmethod
    def get_card_type():
        """
        Keeps prompting a user with a card type option until a user gives
        a valid answer, and returns the selected card type.
        :return: CardType
        """
        card_types = {}
        count = 0
        question = "\n-------- Card type ---------\n"
        for type_ in CardType:
            card_types[count] = type_
            count += 1
            question += f"\t{count}. {type_.value}\n"
        question += "Please select a card type: "
        input_type = None
        while input_type is None:
            try:
                answer = input(question)
                InputHandler.validate_input(len(card_types), answer)
            except ValueError:
                print("\nPlease type an integer!")
            except CommandNotFoundException as e:
                print(f"{e}")
            else:
                input_type = card_types[int(answer) - 1]
                return input_type


class CardNumber:
    """This class represents a unique card number."""

    def __init__(self):
        """Card number will be initialized with a user input."""
        self._card_number = input("Please type your card number: ")

    def __str__(self):
        return f"{self._card_number}"


class CardHolder:
    """This class represents a card holder."""

    def __init__(self):
        """Card holder will be initialized with a user input."""
        self._card_holder = input("Please type the card holder name: ")

    def __str__(self):
        return f"{self._card_holder}"
