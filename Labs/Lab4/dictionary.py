"""This module holds a dictionary class and driver methods that
runs the program."""

import json
from file_handler import FileHandler
from difflib import get_close_matches
from file_handler import InvalidFileTypeError


class WordNotFoundException(Exception):
    """This exception will be raised when there is no matching word found,
    and will suggest similar words."""
    def __init__(self, word, keys):
        close_words = get_close_matches(word, keys)
        super().__init__(f"No exact match found.\n"
                         f"Were you looking for a word among {close_words} ?")


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
        FileHandler.write_lines(path, word)
        for definition in definitions:
            count += 1
            definition = definition.replace('\\n', ' ')
            FileHandler.write_lines(f"{count}. {definition}")

    def load_dictionary(self, filepath):
        """
        It loads data from the given filepath into a dictionary.
        If the file is uccesfully loaded, return True, otherwise return false.
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
        It looks for a given word and returns the definitions.
        if there is no exact match, raise WordNotFoundException
        :param word: String
        :return: List
        """
        if self.dictionary.get(word) is None:
            raise WordNotFoundException(word, self.dictionary.keys())
        return self.dictionary.get(word)

    def run_program(self):
        """
        Keep prompting users with the option to query definitions until
        the user has entered 'exitprogram'.
        """
        EXIT_COMMAND = "exitprogram"
        word = ""
        while word != EXIT_COMMAND:
            word = input("\nPlease type a word to search (Type 'exitprogram'"
                         " if you want to stop the program): ")
            try:
                result = self.query_definition(word)
            except WordNotFoundException as e:
                print(f"{e}")
            else:
                Dictionary.print_query_result(word, result)
                Dictionary.print_query_result(word, result)



def main():
    """Instantiates Dictionary and runs the program."""

    my_dictionary = Dictionary()

    # Loads the dictionary file, if succesful, runs the program.
    if my_dictionary.load_dictionary("data.json"):
        my_dictionary.run_program()


if __name__ == "__main__":
    main()
