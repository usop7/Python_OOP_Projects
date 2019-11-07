"""This module embodies Library class and main method."""

from catalogue import Catalogue
from input_handler import InputHandler
from input_handler import CommandNotFoundException


class Library:
    """This class embodies the basic functions and attributes of a Library."""

    def __init__(self, catalogue):
        """
        Initialize a library with a catalogue.
        :param catalogue: a catalogue object
        """
        self._catalogue = catalogue

    @property
    def catalogue(self):
        return self._catalogue

    def check_out(self, call_number):
        """
        Check out an item with a given call number.
        :param call_number: a String
        """
        self.catalogue.check_out_item(call_number)

    def return_item(self, call_number):
        """
        Return an item with a given call number.
        :param call_number: a String
        """
        self.catalogue.return_item(call_number)

    def give_options(self):
        """
        Prompt the user with the choices.
        """
        options = [self.catalogue.display_available_items,
                   self.catalogue.search,
                   self.check_out,
                   self.return_item,
                   self.catalogue.add_item,
                   self.catalogue.remove_item]
        try:
            answer = input("-------------------------------\n"
                           "(1) Display available items \n"
                           "(2) Find an item by title\n"
                           "(3) Check out an item\n"
                           "(4) Return an item\n"
                           "(5) Add an item\n"
                           "(6) Remove an item\n"
                           "Please select: \n")
            InputHandler.validate(len(options), answer)
            answer = int(answer) - 1
        except ValueError:
            print("\n[Error] Please type an integer!")
        except CommandNotFoundException as e:
            print(f"{e}")
        else:
            if answer == 1:
                title = input("Enter the item title: ")
                options[answer](title)
            elif answer in [2, 3, 5]:
                call_number = input("Enter the call number of the item: ")
                options[answer](call_number)
            else:
                options[answer]()


def main():
    """
    Creates a library and prompts the user with options.
    """

    # Create a new library with a new catalogue
    library = Library(Catalogue())

    # User Prompt
    while True:
        library.give_options()


if __name__ == "__main__":
    main()

