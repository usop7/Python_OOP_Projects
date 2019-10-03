"""This module holds a dictionary class and driver methods that
runs the program."""

import json


class Dictionary:
    """This class represents a dictionary."""

    def __init__(self):
        self.dictionary = {}

    def load_dictionary(self, filepath):
        """
        It loads data from the given filepath into the words list.
        :param filepath: String
        """
        text_file = open(filepath, mode='r', encoding='utf-8')
        data = text_file.read()
        # convert String data to Dictionary format
        self.dictionary = json.loads(data)
        text_file.close()

    def query_definition(self, word):
        """
        It looks for a given word and returns the definitions.
        :param word: String
        :return: List
        """
        definitions = self.dictionary.get(word)
        return definitions

    def test_print(self):
        for key, item in self.dictionary.items():
            print(f"{key}\n {item}\n\n")

    def run_program(self):
        """
        Keep prompting users with the option to query definitions until
        the user has entered 'exitprogram'.
        """
        word = ""
        count = 0
        while word != "exitprogram":
            count = 0
            word = input("Please type a word to search (Type"
                         "'exitprogram' if you want to stop the program)"
                         "the program): ")
            result = self.query_definition(word)
            if result is None:
                print("No word found.\n")
            else:
                print(f"\n---------------------------------------------\n"
                      f"Query Results for [{word}]:")
                for definition in result:
                    count += 1
                    definition = definition.replace('\\n', ' ')
                    print(f"{count}. {definition}")
                print("----------------------------------------------\n")


def main():
    my_dictionary = Dictionary()
    my_dictionary.load_dictionary("data.json")
    my_dictionary.run_program()


if __name__ == "__main__":
    main()





