import difflib
from book import Book


class Library:
    def __init__(self, book_list):
        # dictionary- call_number: book object
        self._book_list = book_list

    def find_books(self, title):
        book_result = []
        for book in self._book_list.values():
            if book.get_title():
                book_result.append(book)
        return book_result

    def add_book(self, new_book):
        if self._book_list.get(str(new_book.get_call_number())) is None:
            self._book_list[new_book.get_call_number()] = new_book

    def remove_book(self, call_number):
        if self._book_list.get(call_number) is not None:
            del self._book_list[call_number]


