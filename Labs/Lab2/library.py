import difflib
from book import Book


class Library:
    def __init__(self, book_list):
        # dictionary- call_number: book object
        self._book_list = book_list

    def find_books(self, title):
        for book in self._book_list.values():
            if book.get_title() == title:
                print(book)

    def add_book(self, new_book):
        if self._book_list.get(str(new_book.get_call_number())) is None:
            self._book_list[new_book.get_call_number()] = new_book
            print("The book is added.")
        else:
            print("This book already exists.")

    def remove_book(self, call_number):
        if self._book_list.get(call_number) is not None:
            del self._book_list[call_number]
            print("The book is removed.")

    def check_out(self, call_number):
        if self._book_list.get(call_number) is not None:
            book = self._book_list.get(call_number)
            if book.check_availability() is True:
                book.decrease_copy()
            else:
                print("No copies unavailable")
        else:
            print("No result found.")

    def return_book(self, call_number):
        if self._book_list.get(call_number) is not None:
            book = self._book_list.get(call_number)
            book.increase_copy()

    def display_available_books(self):
        for book in self._book_list.values():
            if book.check_availability():
                print(book)



