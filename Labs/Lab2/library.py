import difflib
from book import Book


class Library:
    def __init__(self):
        # dictionary- call_number: book object
        self._book_list = {}

    def find_books(self, title):
        count = 0
        for book in self._book_list.values():
            if book.get_title() == title:
                print(book)
                count += 1
        if count == 0:
            print("No result found.")

    def add_book(self, new_book):
        if self._book_list.get(str(new_book.get_call_number())) is None:
            self._book_list[new_book.get_call_number()] = new_book
            print(f"Book({new_book.get_call_number()}) bas been added.")
        else:
            print("This book already exists.")

    def remove_book(self, call_number):
        if self._book_list.get(call_number) is not None:
            del self._book_list[call_number]
            print("The book is removed.")
        else:
            print("No matching call number found.")

    def check_out(self, call_number):
        if self._book_list.get(call_number) is not None:
            book = self._book_list.get(call_number)
            if book.check_availability() is True:
                book.decrease_copy()
                print(f"Book({call_number}) has been checked out.")
            else:
                print("No copies available")
        else:
            print("No matching call number found.")

    def return_book(self, call_number):
        if self._book_list.get(call_number) is not None:
            book = self._book_list.get(call_number)
            book.increase_copy()
            print("Book returned.")
        else:
            print("No matching call number found.")

    def display_available_books(self):
        count = 0
        print("Available books:")
        for book in self._book_list.values():
            count += 1
            if book.check_availability():
                print(book)
        if count == 0:
            print("No books are available")

    def give_options(self):
        options = [self.display_available_books, self.find_books ,self.check_out, self.return_book]
        question = ("-------------------------------\n"
                    "(1) Display available books \n"
                    "(2) Find a book\n"
                    "(3) Check out a book\n"
                    "(4) Return a book\n"
                    "Please select: \n")
        answer = int(input(question))
        if answer == 2:
            title = input("Enter the book title: ")
            options[answer-1](title)
        elif answer == 3 or answer == 4:
            call_number = input("Enter the call number of the book: ")
            options[answer-1](call_number)
        else:
            options[answer-1]()


def main():
    # checkout, return, access catalogue

    # Create a new library
    library = Library()

    # Create books
    book1 = Book("book1", "1", "kim1", 2)
    book2 = Book("book2", "2", "kim2", 2)

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)

    # User Prompt
    while True:
        library.give_options()


if __name__ == "__main__":
    main()

