import abc


class Item(abc.ABC):
    """
    An Abstract Base Class for a library item that provides a simple interface that all
    characters need to implement.
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

    def get_title(self):
        """
        Return the title.
        :return: a String
        """
        return self._title

    def get_call_number(self):
        """
        Return the call number.
        :return: a String
        """
        return self._call_number

    title = property(get_call_number)
    call_number = property(get_call_number)

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
