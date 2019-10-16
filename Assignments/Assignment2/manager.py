"""This module includes . """

from card_info import CardType
from card import CreditCard
from card import IDCard
from card import BusinessCard
from card import MembershipCard
from card import GiftCard
from card import OtherCard
from input_handler import InputHandler
from input_handler import CommandNotFoundException
from file_writer import FileWriter
from datetime import datetime


class Manager:
    """This class represents a Card Manager app."""

    name = "CardManager"

    # Each card will have a sequential unique ID starting from 1.
    id = 0

    @classmethod
    def get_new_id(cls):
        """Increments id by 1, and returns the new id"""
        cls.id += 1
        return cls.id

    def __init__(self):
        self._card_list = {}

    def run_program(self):
        """
        Prompts a user with a various options until a user types 'exit'.
        """
        commands = [self.print_all_cards,
                    self.print_cards_by_type,
                    self.add_card,
                    self.search_card,
                    self.delete_card_by_id,
                    self.delete_card_by_name,
                    self.backup_card_list]
        EXIT = "exit"
        want_to_exit = False
        while not want_to_exit:
            answer = input(f"\nWhat would you like to do?\n"
                           f"\t1. Show all cards in the app\n"
                           f"\t2. Show all cards of a specific type\n"
                           f"\t3. Add a new card\n"
                           f"\t4. Search for a card\n"
                           f"\t5. Delete a card by ID\n"
                           f"\t6. Delete a card by Name\n"
                           f"\t7. Back up all cards in the app\n"
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
        if len(self._card_list) == 0:
            print("\nThere is no card saved.")
        else:
            for card in self._card_list.values():
                print(card)

    def print_cards_by_type(self):
        """Prints all the cards of a specific type."""
        input_type = CardType.set_card_type()
        count = 0
        for card in self._card_list.values():
            if card.type == input_type:
                count += 1
                print(card)
        if count == 0:
            print(f"\nThere is no {input_type.value} saved.")

    def add_card(self):
        """Creates a new card with a new ID, and adds is to the list."""
        new_id = Manager.get_new_id()
        type_map = {
            CardType.ID: IDCard,
            CardType.CREDIT: CreditCard,
            CardType.BUSINESS: BusinessCard,
            CardType.MEMBERSHIP: MembershipCard,
            CardType.GIFT: GiftCard,
            CardType.OTHER: OtherCard
        }
        input_type = CardType.set_card_type()
        self._card_list[new_id] = type_map[input_type](new_id, input_type)
        print("The following card has been successfully added!\n")
        print(self._card_list[new_id])

    def search_card(self):
        """
        Prompts a user with a card name to search, finds close matches,
        and shows the results.
        :return boolean
        """
        word = input("\nPlease type the card name to search: ")
        names = [word.lower(), word.upper(), word.title(), word.capitalize()]
        count = 0
        for card in self._card_list.values():
            if card.name in names:
                count += 1
                print(card)
                return True
        if count == 0:
            print(f"\nThere is no card named '{word}'.")
            return False

    def backup_card_list(self):
        """
        Converts each card into one line of string and saves this collection
        collection to a file named 'CardManager_Export_DDMMYY_HHMM.txt'.
        """
        now = datetime.now()
        path = f"{self.name}_Export_{now.strftime('%d%m%y_%H%M')}.txt"
        card_string_list = []
        saved = False
        for card in self._card_list.values():
            card_string_list.append(card.to_one_line_str())
        try:
            FileWriter.write_lines(path, card_string_list)
        except Exception as e:
            print(f"Unknown Exception Caught: {e}")
        else:
            saved = True
        finally:
            if saved:
                print(f"File has been successfully created at '{path}'")
            else:
                print("Back up failed.")

    def delete_card_by_id(self):
        """Deletes a card by its specific ID.
        :return boolean"""
        answer = input("Type the card ID to delete: ")
        if answer.isdigit() and self._card_list.get(int(answer)) is not None:
            del self._card_list[int(answer)]
            print("Requested card has been successfully deleted.")
            return True
        else:
            print(f"There is no card whose ID is '{answer}'")
            return False

    def delete_card_by_name(self):
        """Deletes card(s) by its name.
        :return boolean"""
        answer = input("Type the card name to delete: ")
        delete_list = []
        count = 0
        # Records card IDs whose name is same as the user input.
        for card in self._card_list.values():
            if card.name == answer:
                count += 1
                delete_list.append(card.id)
        # Deletes the cards from the list.
        for card_id in delete_list:
            del self._card_list[card_id]

        if count == 0:
            print(f"\nThere is no card named '{answer}'.")
            return False
        else:
            print(f"{count} card(s) have been successfully deleted.")
            return True


def main():
    card_manager = Manager()
    card_manager.run_program()


if __name__ == '__main__':
    main()
