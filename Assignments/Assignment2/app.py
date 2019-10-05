"""This module includes . """

from card_info import CardType
from card import CreditCard
from card import IDCard
from card import BusinessCard
from input_handler import InputHandler
from input_handler import CommandNotFoundException


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
        """Increments id by 1, and returns the new id"""
        cls.id += 1
        return cls.id

    def __init__(self):
        self.num_of_cards = 0
        self.card_list = {}

    def run_program(self):
        """
        Keeps prompting users with the option to query a word until
        the user types 'exitprogram'.
        If it succeeds to find a word, prints and saves the definitions.
        """
        commands = [self.print_all_cards,
                    self.print_cards_by_type,
                    self.add_card,
                    self.search_card]
        EXIT = "exit"
        want_to_exit = False
        while not want_to_exit:
            answer = input(f"\nWhat would you like to do?\n"
                           f"\t1. Show all cards in the app\n"
                           f"\t2. Show all cards of a specific type\n"
                           f"\t3. Add a new card\n"
                           f"\t4. Search for a card\n"
                           f"\t4. Delete a card\n"
                           f"\t5. Back up all cards in the app\n"
                           f"Please select or type '{EXIT}' to exit: ")
            if answer == EXIT:
                print("\nBye!")
                want_to_exit = True
            else:
                try:
                    InputHandler.validate_input(len(commands), answer)
                except ValueError:
                    print("\nPlease type an integer!")
                except CommandNotFoundException as e:
                    print(f"{e}")
                else:
                    commands[int(answer) - 1]()

    def print_all_cards(self):
        """Prints all the cards in the list."""
        if len(self.card_list) == 0:
            print("\nThere is no card saved.")
        else:
            for card in self.card_list.values():
                print(card)

    def print_cards_by_type(self):
        """Prints all the cards of a specific type."""
        input_type = CardType.get_card_type()
        count = 0
        for card in self.card_list.values():
            if card.get_type() == input_type:
                count += 1
                print(card)
        if count == 0:
            print(f"\nThere is no {input_type.value} saved.")

    def add_card(self):
        """
        Generates a new id, creates a new card, and adds is to the list.
        """
        new_id = Manager.get_new_id()
        type_map = {
            CardType.ID: IDCard,
            CardType.CREDIT: CreditCard,
            CardType.BUSINESS: BusinessCard
        }
        input_type = CardType.get_card_type()
        self.card_list[new_id] = type_map[input_type](new_id, input_type)
        print("The following card has been successfully added!\n")
        print(self.card_list[new_id])

    def search_card(self):
        """
        Prompts a user with a card name to search, finds close matches,
        and shows the results.
        """
        word = input("\nPlease type the card name to search: ")
        names = [word.lower(), word.upper(), word.title(), word.capitalize()]
        count = 0
        for card in self.card_list.values():
            if card.get_name() in names:
                count += 1
                print(card)
        if count == 0:
            print(f"\nThere is no card named '{word}'.")


def main():
    card_manager = Manager()
    card_manager.run_program()


if __name__ == '__main__':
    main()