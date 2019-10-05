"""This module includes . """

from card_info import CardType
from card import CreditCard


class App:
    """This class represents an app."""

    @staticmethod
    def user_input_handler(num_commands, user_input):
        if not user_input.isdigit():
            raise ValueError
        if int(user_input) < 1 or int(user_input) > num_commands:
            raise CommandNotFoundException(num_commands)

    def __init__(self):
        self.manager = Manager()


class CommandNotFoundException(Exception):
    """
    This exception will be raised when there is no matching command found.
    """

    def __init__(self, num_commands):
        super().__init__(f"\nPlease select between 1 to {num_commands}")


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
        commands = [self.add_card, self.print_all_cards,
                    self.print_cards_by_type]
        EXIT = "exit"
        want_to_exit = False
        while not want_to_exit:
            answer = input(f"\nWhat would you like to do?\n"
                           f"\t1. Add a new card\n"
                           f"\t2. Show all cards in the app\n"
                           f"\t3. Show all cards of a specific type\n"
                           f"\t4. Delete a card\n"
                           f"\t5. Back up all cards in the app\n"
                           f"Please select or type '{EXIT}' to exit): ")
            if answer == EXIT:
                print("\nBye!")
                want_to_exit = True
            else:
                try:
                    App.user_input_handler(len(commands), answer)
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
            for card in self.card_list:
                print(card)

    def print_cards_by_type(self):
        """Prints all the cards of a specific type."""
        input_type = CardType.set_card_type()
        count = 0
        for card in self.card_list:
            if card.get_type() == input_type:
                count += 1
                print(card)
        if count == 0:
            print(f"\nThere is no {input_type.value} saved.")

    def add_card(self):
        """
        Generates a new id, creates a new card, and add is to the list.
        """
        new_id = Manager.get_new_id()
        input_type = CardType.set_card_type()
        if input_type == CardType.CREDIT:
            self.card_list[new_id] = CreditCard(new_id, input_type)
        # Prints the newly created card
        print(self.card_list[new_id])


def main():
    card_manager = Manager()
    card_manager.run_program()


if __name__ == '__main__':
    main()