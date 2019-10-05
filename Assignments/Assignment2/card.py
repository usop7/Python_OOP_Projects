"""This module includes classes related to card."""

import abc
from card_info import CardNumber
from card_info import CardHolder


class Card(abc.ABC):
    """
    This class serves as a base class and should be inherited from
    a specific card type class.
    """

    def __init__(self, id_, type_):
        self._id = id_  # will be auto assigned by a card manager
        self._name = None
        self.set_name()
        self._type_ = type_

    def set_name(self):
        """Set card name with the user input."""
        self._name = input("Please type the card name: ")

    def get_type(self):
        return self._type_

    def __str__(self):
        pass

    type_ = property(get_type)


class CreditCard(Card):
    """This class represents a Credit Card."""

    def __init__(self, id_, type_):
        super().__init__(id_, type_)
        self._number = CardNumber()
        self._card_holder = CardHolder()
        #self._company = company
        #self._cvc_number = cvc_number
        #self._expiry_date = expiry_date

    def __str__(self):
        return f"-----------------------------------------\n" \
               f"(ID: {self._id}) {self._name}\n" \
               f"\ttype: {self._type_.value}\n" \
               f"\tnumber: {self._number}\n" \
               f"\tcard holder: {self._card_holder}\n" \
               f"-----------------------------------------\n"

