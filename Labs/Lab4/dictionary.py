"""This module holds a dictionary class and driver methods that
runs the program."""

import json
from file_handler import FileHandler
from difflib import get_close_matches
from file_handler import InvalidFileTypeError


class WordNotFoundException(Exception):
    """
    This exception will be raised when there is no matching word found.
    If there are close matches, it will suggest those words.
    """
    def __init__(self, word, keys):
        close_words = get_close_matches(word, keys)
        if len(close_words) == 0:
            super().__init__("No match found.")
        else:
            super().__init__(f"No exact match found.\nWere you looking for "
                             f"a word among {close_words} ?")


class Dictionary:
    """This class represents a dictionary."""

    def __init__(self):
        self.dictionary = {}

    @classmethod
    def print_query_result(cls, word, definitions):
        """
        Prints out the word and the definitions.
        :param word: String
        :param definitions: List
        """
        count = 0
        print(f"\n---------------------------------------------\n"
              f"Query Results for [{word}]:")
        for definition in definitions:
            count += 1
            definition = definition.replace('\\n', ' ')
            print(f"{count}. {definition}")
        print("----------------------------------------------")

    @classmethod
    def save_query_result(cls, path, word, definitions):
        """
        Appends the word and the definitions into a text file.
        :param path: String
        :param word: String
        :param definitions: List
        """
        count = 0
        try:
            FileHandler.write_lines(path, f"\n{word}")
        except Exception as e:
            print(f"Query result was not saved.\n"
                  f"Unknown Exception caught: {e}")
        else:
            for definition in definitions:
                count += 1
                definition = definition.replace('\\n', ' ')
                FileHandler.write_lines(path, f"{count}. {definition}")

    def load_dictionary(self, filepath):
        """
        It loads data from the given filepath into a dictionary.
        If the file load was successful, returns True, otherwise returns false.
        :param filepath: String
        :return: boolean
        """
        loaded = False
        try:
            self.dictionary = json.loads(FileHandler.load_data(filepath))
        except FileNotFoundError as e:
            print(f"{e}")
        except InvalidFileTypeError as e:
            print(f"{e}")
        except json.decoder.JSONDecodeError as e:
            print(f"Input file format is not compatible for dictionary: {e}")
        except Exception as e:
            print(f"Unknown Exception caught: {e}")
        else:
            loaded = True
        finally:
            return loaded

    def query_definition(self, word):
        """
        It looks for a given word in the dictionary and returns definitions.
        if there is no exact match found, looks for the word with various
        cases (capitilized, lowercase, uppercase, and titled).
        If none of above exists, raises WordNotFoundException error.
        :param word: String
        :return: List
        """
        if self.dictionary.get(word) is not None:
            return self.dictionary.get(word)
        elif self.dictionary.get(word.capitalize()) is not None:
            return self.dictionary.get(word.capitalize())
        elif self.dictionary.get(word.lower()) is not None:
            return self.dictionary.get(word.lower())
        elif self.dictionary.get(word.upper()) is not None:
            return self.dictionary.get(word.upper())
        elif self.dictionary.get(word.title()) is not None:
            return self.dictionary.get(word.title())
        else:
            raise WordNotFoundException(word, self.dictionary.keys())

    def run_program(self):
        """
        Keeps prompting users with the option to query a word until
        the user types 'exitprogram'.
        """
        EXIT_COMMAND = "exitprogram"
        want_to_exit = False
        while not want_to_exit:
            word = input("\nPlease type a word to search (Type 'exitprogram'"
                         " if you want to stop the program): ")
            if word == EXIT_COMMAND:
                want_to_exit = True
            else:
                try:
                    result = self.query_definition(word)
                except WordNotFoundException as e:
                    print(f"{e}")
                else:
                    Dictionary.print_query_result(word, result)
                    Dictionary.save_query_result("result.txt", word, result)


def main():
    """Instantiates Dictionary and runs the program."""

    my_dictionary = Dictionary()

    # Loads the dictionary file, if successful, runs the dictionary program.
    input_data_path = input("Type the dictionary file path: ")
    if my_dictionary.load_dictionary(input_data_path):
        my_dictionary.run_program()


if __name__ == "__main__":
    main()
