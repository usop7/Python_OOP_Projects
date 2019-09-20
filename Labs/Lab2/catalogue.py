from book import Book
from libraryItemGenerator import LibraryItemGenerator as LibGen


class Catalogue:
    def __init__(self):
        self.item_list = {}

    def search(self, title):
        count = 0
        for item in self.item_list.values():
            if item.get_title() == title:
                print(item)
                count += 1
        if count == 0:
            print("No result found.")

    def add_item(self):
        item = LibGen.create_item()
        if self.item_list.get(str(item.get_call_number())) is None:
            self.item_list[item.get_call_number()] = item
            print(f"Item({item.get_call_number()}) bas been added.")
        else:
            print("This item already exists.")

    def remove_item(self, call_number):
        if self.item_list.get(call_number) is not None:
            del self.item_list[call_number]
            print("The book is removed.")
        else:
            print("No matching call number found.")

    def display_available_items(self):
        count = 0
        print("Available Items:")
        for item in self.item_list.values():
            if item.check_availability():
                count += 1
                print(item)
        if count == 0:
            print("No items are available")

