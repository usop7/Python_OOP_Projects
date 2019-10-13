"""This module holds classes regarding card information."""

from enum import Enum
from input_handler import InputHandler
from input_handler import CommandNotFoundException


class CardType(Enum):
    ID = "ID Card"
    CREDIT = "Credit Card"
    GIFT = "Gift Card"
    MEMBERSHIP = "Membership Card"
    BUSINESS = "Business Card"
    OTHER = "Other Types of Card"

    @staticmethod
    def set_card_type():
        """
        Keeps prompting a user with a card type option until a user gives
        a valid answer, and returns the selected card type.
        :return: CardType
        """
        card_types = {}
        count = 0
        question = "\nWhich type of card would you like to add?\n"
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


class ExpiryDate:
    """This class represents an expiry date of a card."""

    def __init__(self):
        """Expire date will be initialized with a user input."""
        self._expiry_date = input("Please type the expiry date: ")

    def __str__(self):
        return f"{self._expiry_date}"


class PhoneNumber:
    """This class represents a phone number."""

    def __init__(self):
        """Phonen umber will be initialized with a user input."""
        self._phone_number = input("Please type the phone number: ")

    def __str__(self):
        return f"{self._phone_number}"


class Address:
    """This class represents an address."""

    def __init__(self):
        """Address will be initialized with a user input."""
        self._address = input("Please type the address: ")

    def __str__(self):
        return f"{self._address}"


class Amount:
    """This class represents an amount."""

    def __init__(self):
        """Amount will be initialized with a user input."""
        self._amount = input("Please type the amount: ")

    def __str__(self):
        return f"{self._amount}"
