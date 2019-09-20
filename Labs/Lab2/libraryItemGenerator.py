from book import Book
from journal import Journal
from dvd import DVD


class LibraryItemGenerator:
    """This class embodies a function to generate a library item."""

    @staticmethod
    def create_item():
        """
        Create an item based on user inputs and returns the item object.
        It will prompt the user with various questions based on the item type.
        :return: an item object
        """
        item = None

        # Repeat until the user enters valid types of an item.
        item_type = None
        while item_type not in ["book", "dvd", "journal"]:
            item_type = input("Item Type (Book, DVD, Journal): ").lower()

        # Common questions about an item.
        title = input("Title: ")
        call_number = input("Call Number: ")
        num_copies = int(input("Number of Copies: "))

        # Ask additional questions based on the type of an item.
        if item_type == "book":
            author = input("Author: ")
            item = Book(title, call_number, num_copies, author)
        elif item_type == "dvd":
            release_date = input("Release Date: ")
            region_code = input("Region Code: ")
            item = DVD(title, call_number, num_copies, release_date, region_code)
        elif item_type == "journal":
            issue_number = input("Issue Number: ")
            publisher = input("Publisher: ")
            item = Journal(title, call_number, num_copies, issue_number, publisher)
        else:
            print("Wrong Type")

        return item
