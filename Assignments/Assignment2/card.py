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
        self._info_list = {
            "id": id_,
            "type": type_,
            "name": input("Please type the card name: ")
        }

    def get_type(self):
        return self._info_list["type"]

    def __str__(self):
        info_str = "---------------------------------\n"
        for key, value in self._info_list.items():
            info_str += f"{key}: {value}\n"
        info_str += "---------------------------------\n"
        return info_str


class CreditCard(Card):
    """This class represents a Credit Card."""

    def __init__(self, id_, type_):
        super().__init__(id_, type_)
        self._info_list["number"] = CardNumber()
        self._info_list["card holder"] = CardHolder()
        self._info_list["expiry date"] = ExpiryDate()
        self._info_list["CVC number"] = input("Please type CVC number: ")


