"""This module includes classes related to card."""

import abc
from card_info import CardNumber
from card_info import CardHolder
from card_info import ExpiryDate
from card_info import PhoneNumber
from card_info import Address
from card_info import Amount


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

    def get_id(self):
        return self._id

    def get_type(self):
        return self._type_

    def get_name(self):
        return self._name

    def add_note(self):
        self._extra_info["Note"] = input("Add a note: ")

    def to_one_line_str(self):
        """
        Returns one line of string about the card.
        :return: String
        """
        return self.__str__().replace("\n", ", ").replace("\t", "")

    def __str__(self):
        info_str = f"[ID: {self._id}] {self._name}\n" \
                   f"\tCard Type: {self._type_.value}\n"
        for key, value in self._extra_info.items():
            info_str += f"\t{key}: {value}\n"
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


class BusinessCard(Card):
    """This class represents a Business Card."""

    def __init__(self, id_, type_):
        super().__init__(id_, type_)
        self._extra_info["Phone Number"] = PhoneNumber()
        self._extra_info["Address"] = Address()
        self.add_note()


class MembershipCard(Card):
    """This class represents a Membership Card."""

    def __init__(self, id_, type_):
        super().__init__(id_, type_)
        self._extra_info["Membership Number"] = CardNumber()
        self._extra_info["Card Holder"] = CardHolder()
        self._extra_info["Expiry Date"] = ExpiryDate()
        self.add_note()


class GiftCard(Card):
    """This class represents a Gift Card."""

    def __init__(self, id_, type_):
        super().__init__(id_, type_)
        self._extra_info["Card Number"] = CardNumber()
        self._extra_info["Gift Amount"] = Amount()
        self._extra_info["Expiry Date"] = ExpiryDate()
        self.add_note()


class OtherCard(Card):
    """This class represents a Other type of Card."""

    def __init__(self, id_, type_):
        super().__init__(id_, type_)
        self.add_note()

