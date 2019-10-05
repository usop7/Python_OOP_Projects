"""This module includes . """

from card import CardType
from card import CreditCard

class App:
    """This class represents an app."""

    def __init__(self):
        self.manager = Manager()


class Manager:
    """This class represents """

    # Each card will have a sequential unique ID starting from 1.
    id = 0

    @classmethod
    def get_new_id(cls):
        """Increases id by 1, and returns the new id"""
        cls.id += 1
        return cls.id

    def __init__(self):
        self.num_of_cards = 0
        self.card_list = {}

    def add_card(self):
        card_types = CardType.set_card_type()
        if card_types == CardType.CREDIT:
            CreditCard(Manager.get_new_id(), card_types)


def main():
    card_manager = Manager()
    card_manager.add_card()


if __name__ == '__main__':
    main()