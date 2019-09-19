from item import Item


class Journal(Item):
    def __init__(self, name, call_number, num_copies, issue_number, publisher):
        super().__init__(name, call_number, num_copies)
        self._publisher = publisher
        self._issue_number = issue_number

    def __str__(self):
        description = (f"title: {self._title}, call number: {self._call_number}, issue number: {self._issue_number},"
                       f"publisher: {self._author}, number of copies: {self._num_copies}")
        return description
