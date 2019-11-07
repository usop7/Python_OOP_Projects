"""This module holds an abstract class Item and its child classes."""

import abc


class Item(abc.ABC):
    """
    An Abstract Base Class for a library item that provides a simple interface
    that all characters need to implement.
    """

    def __init__(self, title, call_number, num_copies):
        """
        Initialize an Item.
        :param title: a String
        :param call_number: a String
        :param num_copies: an int
        """
        self._title = title
        self._call_number = call_number
        self._num_copies = num_copies

    def check_availability(self):
        """
        Return true if an item currently has more than one copy.
        :return: boolean
        """
        return self._num_copies >= 1

    @property
    def title(self):
        """
        Return the title.
        :return: a String
        """
        return self._title

    @property
    def call_number(self):
        """
        Return the call number.
        :return: a String
        """
        return self._call_number

    def increase_copy(self):
        """
        Increase the number of copies by 1.
        """
        self._num_copies += 1

    def decrease_copy(self):
        """
        Decrease the number of copies by 1.
        """
        self._num_copies -= 1

    @abc.abstractmethod
    def __str__(self):
        """
        Any object that inherits from this class must implement this method.
        """
        pass


class Book(Item):
    """This class embodies the str method and attributes of a book."""

    def __init__(self, name, call_number, num_copies, author):
        """
        Initialize a book.
        :param name: a String
        :param call_number: a String
        :param num_copies: an int
        :param author: a String
        """
        super().__init__(name, call_number, num_copies)
        self._author = author

    def __str__(self):
        """
        :return: A well formatted string depicting the book attributes.
        """
        description = (f"[Book] title: {self._title}, "
                       f"call number: {self._call_number}, "
                       f"author: {self._author}, "
                       f"number of copies: {self._num_copies}")
        return description


class DVD(Item):
    """This class embodies the str method and attributes of a dvd."""

    def __init__(self, name, call_number, num_copies, release_date, region_code):
        """
        Initialize a DVD.
        :param name: a String
        :param call_number: a String
        :param num_copies: an int
        :param release_date: a String
        :param region_code: a String
        """
        super().__init__(name, call_number, num_copies)
        self._release_date = release_date
        self._region_code = region_code

    def __str__(self):
        """
        :return: A user friendly formatted string depicting the dvd attributes.
        """
        description = (f"[DVD] title: {self._title}, "
                       f"call number: {self._call_number}, "
                       f"release date: {self._release_date},"
                       f"region code: {self._region_code}, "
                       f"number of copies: {self._num_copies}")
        return description


class Journal(Item):
    """This class embodies the str method and attributes of a journal."""

    def __init__(self, name, call_number, num_copies, issue_number, publisher):
        """
        Initialize a journal.
        :param name: a String
        :param call_number: a String
        :param num_copies: an int
        :param issue_number: a String
        :param publisher: a String
        """
        super().__init__(name, call_number, num_copies)
        self._publisher = publisher
        self._issue_number = issue_number

    def __str__(self):
        """
        :return: A well formatted string depicting the journal attributes.
        """
        description = (f"[Journal] title: {self._title}, "
                       f"call number: {self._call_number}, "
                       f"issue number: {self._issue_number},"
                       f"publisher: {self._publisher}, "
                       f"number of copies: {self._num_copies}")
        return description


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
