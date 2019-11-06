from difflib import get_close_matches
from libraryItemGenerator import LibraryItemGenerator as LibGen
from book import Book
from dvd import DVD


class Catalogue:
    """This class embodies basic functions and attributes of a Catalogue."""

    def __init__(self):
        """
        Initialize an item list of the catalogue.
        """
        # Item Dictionary (key: call number, value: Item object)
        self.item_list = {}

        # Add some items manually for testing purposes.
        book1 = Book("In praise of Idleness", "B-1", 3, "bertrand russell")
        book2 = Book("Breaking the Code", "B-2", 1, "Pat Matter")
        dvd = DVD("Breaking Bad", "D-1", 2, "2019-01-05", "CA")
        self._add_item_by_item(book1)
        self._add_item_by_item(book2)
        self._add_item_by_item(dvd)

    def get_close_matches_by_title(self, title):
        """
        Returns a list of close matches by an item's title.
        :param title: a String
        :return: a list of String
        """
        titles = []
        for item in self.item_list.values():
            titles.append(item.title)
        return get_close_matches(title, titles)

    def search(self, title):
        """
        Search an item by a title and prints items that have similar titles.
        :param title: a String
        """
        close_matches = self.get_close_matches_by_title(title)
        count = 0
        for item in self.item_list.values():
            if item.title in close_matches:
                print(item)
                count += 1
        if count == 0:
            print("No result found.")

    def item_exists(self, call_number):
        """
        Return true if an item already exists.
        It is determined by an item's call number.
        :param call_number: a String
        :return: boolean
        """
        return call_number in self.item_list.keys()

    def get_item(self, call_number):
        """
        Return an item by call number
        :param call_number: a String
        :return: an Item object
        """
        return self.item_list.get(call_number)

    def add_item(self):
        """
        Adds a new item to the catalogue if not exists yet.
        """
        item = LibGen.create_item()
        if not self.item_exists(item.call_number):
            self.item_list[item.call_number] = item
            print(f"Item({item.call_number}) bas been added.")
        else:
            print("This item already exists.")

    def _add_item_by_item(self, item):
        """
        This method will be used for testing purposes.
        It takes an item object as a parameter and adds it to the item list.
        :param item: an item object
        """
        self.item_list[item.call_number] = item

    def remove_item(self, call_number):
        """
        Finds an item by call number, and remove it if exists.
        :param call_number: a String
        """
        if self.item_exists(call_number):
            del self.item_list[call_number]
            print(f"The item({call_number}) is removed.")
        else:
            print("No matching call number found.")

    def display_available_items(self):
        """Display all available items that have more than one copy
        in the catalogue."""
        count = 0
        print("Available Items:")
        for item in self.item_list.values():
            if item.check_availability():
                count += 1
                print(item)
        if count == 0:
            print("No items are available")

    def check_out_item(self, call_number):
        """
        Check if there exists an item with the call number, and then,
        1) If exists and available, decrease the number of copies.
        2) If exists and not available, notify the user.
        3) If not exists, notify the user.
        :param call_number: a String
        """
        item = self.get_item(call_number)
        if item is not None:
            if item.check_availability() is True:
                item.decrease_copy()
                print(f"Item({call_number}) has been checked out.")
            else:
                print("No copies are available")
        else:
            print("No matching call number found.")

    def return_item(self, call_number):
        """
        Check if there exists an item with the call number, and then,
        1) If exists, increase the number of copies.
        2) If not exists, notify the user.
        :param call_number: a String
        """
        item = self.get_item(call_number)
        if item is not None:
            item.increase_copy()
            print(f"Item({call_number}) returned.")
        else:
            print("No matching call number found.")


