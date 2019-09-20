from item import Item


class Book(Item):
    def __init__(self, name, call_number, num_copies, author):
        super().__init__(name, call_number, num_copies)
        self._author = author

    def __str__(self):
        description = (f"[Book] title: {self._title}, call number: {self._call_number},"
                       f"author: {self._author}, number of copies: {self._num_copies}")
        return description
