import difflib
from catalogue import Catalogue


class Library:
    def __init__(self, catalogue):
        self.catalogue = catalogue

    def access_item_list(self):
        return self.catalogue.item_list

    def check_out(self, call_number):
        item_list = self.access_item_list()
        if item_list.get(call_number) is not None:
            item = item_list.get(call_number)
            title = item.get_title()
            if item.check_availability() is True:
                item.decrease_copy()
                print(f"Item({title}) has been checked out.")
            else:
                print("No copies available")
        else:
            print("No matching call number found.")

    def return_item(self, call_number):
        item_list = self.access_item_list()
        if item_list.get(call_number) is not None:
            item = item_list.get(call_number)
            item.increase_copy()
            print(f"Item({call_number}) returned.")
        else:
            print("No matching call number found.")

    def give_options(self):
        options = [self.catalogue.display_available_items, self.catalogue.search,
                   self.check_out, self.return_item, self.catalogue.add_item, self.catalogue.remove_item]
        answer = 0
        while answer not in ["1", "2", "3", "4", "5", "6"]:
            answer = input("-------------------------------\n"
                           "(1) Display available items \n"
                           "(2) Find an item\n"
                           "(3) Check out an item\n"
                           "(4) Return an item\n"
                           "(5) Add an item\n"
                           "(6) Remove an item\n"
                           "Please select: \n")
        answer = int(answer)
        if answer == 2:
            title = input("Enter the item title: ")
            options[answer-1](title)
        elif answer in [3, 4, 6]:
            call_number = input("Enter the call number of the item: ")
            options[answer-1](call_number)
        else:
            options[answer-1]()


def main():

    # Create a new catalogue
    catalogue = Catalogue()

    # Create a new library with the catalogue created
    library = Library(catalogue)

    # User Prompt
    while True:
        library.give_options()


if __name__ == "__main__":
    main()

