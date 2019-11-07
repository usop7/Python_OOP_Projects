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


class ItemFactory(abc.ABC):
    """
    The ItemFactory class is the base class that the rest of the system
    depends on. It defines a factory interface that creates an Item.
    """

    @abc.abstractmethod
    def create_item(self) -> Item:
        pass


class BookFactory(ItemFactory):
    """The BookFactory is responsible for creating a Book Item."""

    @abc.abstractmethod
    def create_item(self) -> Item:
        title = input("Title: ")
        call_number = input("Call Number: ")
        num_copies = int(input("Number of Copies: "))
        author = input("Author: ")
        return Book(title, call_number, num_copies, author)


class DvdFactory(ItemFactory):
    """The DvdFactory is responsible for creating a DVD Item."""

    @abc.abstractmethod
    def create_item(self) -> Item:
        title = input("Title: ")
        call_number = input("Call Number: ")
        num_copies = int(input("Number of Copies: "))
        release_date = input("Release Date: ")
        region_code = input("Region Code: ")
        return DVD(title, call_number, num_copies, release_date, region_code)


class JournalFactory(ItemFactory):
    """The JournalFactory is responsible for creating a Journal Item."""

    @abc.abstractmethod
    def create_item(self) -> Item:
        title = input("Title: ")
        call_number = input("Call Number: ")
        num_copies = int(input("Number of Copies: "))
        issue_number = input("Issue Number: ")
        publisher = input("Publisher: ")
        return Journal(title, call_number, num_copies, issue_number, publisher)
