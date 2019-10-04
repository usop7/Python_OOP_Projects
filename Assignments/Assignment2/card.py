"""This module includes classes related to card."""

import abc
from enum import Enum


class CardType(Enum):
    ID = "ID Card"
    CREDIT = "Credit Card"
    GIFT = "Gift Card"
    MEMBERSHIP = "Membership Card"
    LOYALTY = "Loyalty Card"
    BUSINESS = "Business Card"
    OTHER = "Other"

    @classmethod
    def select_card_types(cls):
        card_types = {}
        count = 0
        question = "-------- Card Category ---------"
        for type_ in CardType:
            card_types[count] = type_
            question += f"{count+1}. {type_.value}"
        question += "Please select a card category: "

        select = int(input(question))
        return card_types[select-1]


class Card(abc.ABC):
    """
    This class serves as a base class and should be inherited from
    a specific card type class.
    """

    # Each card will have a sequential unique ID starting from 1.
    id = 0

    @classmethod
    def get_new_id(cls):
        """Increases id by 1, and returns the new id"""
        cls.id += 1
        return cls.id

    def __init__(self, category, note=None):
        self._id = Card.get_new_id()
        self._category = category
        self._note = note

    def get_category(self):
        return self._category

    def __str__(self):
        pass

    category = property(get_category)


class CreditCard(Card):
    """This class represents a Credit Card."""

    def __init__(self, category, type_, number, card_holder, company,
                 cvc_number, expiry_date):
        super().__init__(category)
        self._type_ = type_
        self._number = number
        self._card_holder = card_holder
        self._company = company
        self._cvc_number = cvc_number
        self._expiry_date = expiry_date

    def __str__(self):
        return f"{self._type_.value}: {self._company}"


class IDCard(Card):
    """This class represents a Credit Card."""

    def __init__(self, category, id, card_holder, provider, expiry_date=None,
                 extra_info=None):
        super().__init__(category)
        self._id = id
        self._card_holder = card_holder
        self._provider = provider
        self._expiry_date = expiry_date
        self._extra_info = extra_info

    def __str__(self):
        return f"{self._category}: {self._provider}"

