"""This module holds a dictionary class and driver methods that
runs the program."""

import json
from file_handler import FileHandler


class Dictionary:
    """This class represents a dictionary."""

    def __init__(self):
        self.dictionary = {}

    def load_dictionary(self, filepath):
        """
        It loads data from the given filepath into the words list.
        :param filepath: String
        """
        data = FileHandler.load_data(filepath)
        # convert String data to Dictionary format
        self.dictionary = json.loads(data)

    def query_definition(self, word):
        """
        It looks for a given word and returns the definitions.
        :param word: String
        :return: List
        """
        definitions = self.dictionary.get(word)
        return definitions

    def run_program(self):
        """
        Keep prompting users with the option to query definitions until
        the user has entered 'exitprogram'.
        """
        EXIT_COMMAND = "exitprogram"
        word = ""
        while word != EXIT_COMMAND:
            word = input("Please type a word to search (Type 'exitprogram'"
                         "if you want to stop the program): ").lower()
            result = self.query_definition(word)
            count = 0  # It counts the number of definitions.

            if word == EXIT_COMMAND:
                return
            elif result is None:
                print("No word found.\n")
            else:
                print(f"\n---------------------------------------------\n"
                      f"Query Results for [{word}]:")
                for definition in result:
                    count += 1
                    definition = definition.replace('\\n', ' ')
                    print(f"{count}. {definition}")
                print("----------------------------------------------\n")

                # Records the result in the text file.
                FileHandler.write_lines("result.txt", f"{word}:\n{result}\n")


def main():
    my_dictionary = Dictionary()

    try:
        my_dictionary.load_dictionary("data.json")
    except FileNotFoundError as e:
        print(f"{e}")
    except TypeError as e:
        print(f"{e}")
    else:
        my_dictionary.run_program()


if __name__ == "__main__":
    main()
