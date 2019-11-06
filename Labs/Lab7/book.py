from item import Item


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
        :return: A user friendly formatted string depicting the book attributes.
        """
        description = (f"[Book] title: {self._title}, call number: {self._call_number}, "
                       f"author: {self._author}, number of copies: {self._num_copies}")
        return description
