"""This module includes classes related to card."""

import abc
from card_info import CardNumber
from card_info import CardHolder
from card_info import ExpiryDate


class Card(abc.ABC):
    """
    This class serves as a base class and should be inherited from
    a specific card type class.
    """

    def __init__(self, id_, type_):
        self._id = id_
        self._type_ = type_
        self._name = input("Please type the card name: ")
        self._extra_info = {}

    def get_type(self):
        return self._type_

    def get_name(self):
        return self._name

    def add_note(self):
        self._extra_info["Note"] = input("Extra Note: ")

    def __str__(self):
        info_str = "---------------------------------\n" \
                   f"({self._id}) {self._name}\n" \
                   f"Card Type:{self._type_.value}\n"
        for key, value in self._extra_info.items():
            info_str += f"{key}: {value}\n"
        info_str += "---------------------------------\n"
        return info_str


class CreditCard(Card):
    """This class represents a Credit Card."""

    def __init__(self, id_, type_):
        super().__init__(id_, type_)
        self._extra_info["Card Number"] = CardNumber()
        self._extra_info["Card Holder"] = CardHolder()
        self._extra_info["Expiry Date"] = ExpiryDate()
        self._extra_info["CVC Number"] = input("Please type CVC number: ")
        self.add_note()


class IDCard(Card):
    """This class represents a ID Card."""

    def __init__(self, id_, type_):
        super().__init__(id_, type_)
        self._extra_info["ID Number"] = CardNumber()
        self._extra_info["Card Holder"] = CardHolder()
        self._extra_info["Expiry Date"] = ExpiryDate()
        self.add_note()


