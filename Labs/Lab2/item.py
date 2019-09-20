import abc


class Item(abc.ABC):
    def __init__(self, title, call_number, num_copies):
        self._title = title
        self._call_number = call_number
        self._num_copies = num_copies

    def check_availability(self):
        return self._num_copies >= 1

    def get_title(self):
        return self._title

    def get_call_number(self):
        return self._call_number

    def increase_copy(self):
        self._num_copies += 1

    def decrease_copy(self):
        self._num_copies -= 1

    @abc.abstractmethod
    def __str__(self):
        pass
