class Book:
    def __init__(self, title, call_number, author, num_copies):
        self._title = title
        self._call_number = call_number
        self._author = author
        self._num_copies = num_copies

    def check_availability(self):
        return self._num_copies >= 1

    def __str__(self):
        return f"title: {self._title}, call number: {self._call_number}, author: {self._author}, number of copies: {self._num_copies}"

    