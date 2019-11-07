"""This module embodies Library class and main method."""

from catalogue import Catalogue


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
        answer = 0

        # Create a list of valid answers
        valid_answers = []
        i = 1
        while i <= len(options):
            valid_answers.append(str(i))
            i += 1

        # Repeat until the user enters the valid options (1~6)
        while answer not in valid_answers:
            answer = input("-------------------------------\n"
                           "(1) Display available items \n"
                           "(2) Find an item\n"
                           "(3) Check out an item\n"
                           "(4) Return an item\n"
                           "(5) Add an item\n"
                           "(6) Remove an item\n"
                           "Please select: \n")
        answer = int(answer)

        if answer == 2:
            title = input("Enter the item title: ")
            options[answer-1](title)
        elif answer in [3, 4, 6]:
            call_number = input("Enter the call number of the item: ")
            options[answer-1](call_number)
        else:
            options[answer-1]()


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

