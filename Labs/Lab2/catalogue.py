from difflib import get_close_matches
from libraryItemGenerator import LibraryItemGenerator as LibGen


class Catalogue:
    """This class embodies the basic functions and attributes of a Catalogue."""

    def __init__(self):
        """
        Initialize an item list of the catalogue.
        """
        # Item Dictionary (key: call number, value: Item object)
        self.item_list = {}

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
        """
        Display all available items that have more than one copy in the catalogue.
        """
        count = 0
        print("Available Items:")
        for item in self.item_list.values():
            if item.check_availability():
                count += 1
                print(item)
        if count == 0:
            print("No items are available")

