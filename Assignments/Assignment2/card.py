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


class Card(abc.ABC):
    """
    This class serves as a base class and should be inherited from
    a specific card type class.
    """

    def __init__(self, category):
        self._category = category

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
        return f"{self.category.value}: {self._provider}"

