from item import Item


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
        :return: A user friendly formatted string depicting the journal attributes.
        """
        description = (f"[Journal] title: {self._title}, call number: {self._call_number}, "
                       f"issue number: {self._issue_number},"
                       f"publisher: {self._publisher}, number of copies: {self._num_copies}")
        return description
