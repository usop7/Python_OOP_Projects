from item import Item


class DVD(Item):
    """This class embodies the str method and attributes of a dvd."""

    def __init__(self, name, call_number, num_copies, release_date, region_code):
        """
        Initialize a DVD.
        :param name: a String
        :param call_number: a String
        :param num_copies: an int
        :param release_date: a datetime
        :param region_code: a String
        """
        super().__init__(name, call_number, num_copies)
        self._release_date = release_date
        self._region_code = region_code

    def __str__(self):
        """
        :return: A user friendly formatted string depicting the dvd attributes.
        """
        description = (f"[DVD] title: {self._title}, call number: {self._call_number}, "
                       f"release date: {self._release_date},"
                       f"region code: {self._region_code}, number of copies: {self._num_copies}")
        return description
