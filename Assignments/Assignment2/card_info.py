"""This module holds classes regarding card information."""

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
    def set_card_type(cls):
        card_types = {}
        count = 0
        question = "-------- Card type_ ---------"
        for type_ in CardType:
            card_types[count] = type_
            question += f"{count+1}. {type_.value}"
        question += "Please select a card type: "

        select = int(input(question))
        return card_types[select-1]


class CardNumber():
    """This class represents a unique card number."""

    @classmethod
    def set_card_number(cls):
        user_input = input("Please type the card number: ")
        return user_input

    def __init__(self):
        self.number = CardNumber().set_card_number()