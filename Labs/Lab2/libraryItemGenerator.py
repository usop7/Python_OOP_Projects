from book import Book
from journal import Journal
from dvd import DVD


class LibraryItemGenerator:

    @staticmethod
    def create_item():
        item = None
        while item is None:
            item_type = input("Item Type (Book, DVD, Journal): ")
            title = input("Title: ")
            call_number = input("Call Number: ")
            num_copies = input("Number of Copies: ")
            if item_type == "Book":
                author = input("Author: ")
                item = Book(title, call_number, num_copies, author)
            elif item_type == "DVD":
                release_date = input("Release Date: ")
                region_code = input("Region Code: ")
                item = DVD(title, call_number, num_copies, release_date, region_code)
            elif item_type == "Journal":
                issue_number = input("Issue Number: ")
                publisher = input("Publisher: ")
                item = Journal(title, call_number, num_copies, issue_number, publisher)
            else:
                print("Wrong Type")
        return item
