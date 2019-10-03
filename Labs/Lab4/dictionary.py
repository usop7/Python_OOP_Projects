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

    def load_dictionary(self, filepath):
        """
        It loads data from the given filepath into a dictionary.
        If file as succesfully loaded, return True, otherwise return false.
        :param filepath: String
        :return: boolean
        """
        self.dictionary = json.loads(FileHandler.load_data(filepath))

    def write_query_result(self, filepath, word, definitions):
        """
        It appends the query result into a text file.
        :param filepath: String
        :param result: Dictionary
        """
        FileHandler.write_lines(filepath, word)
        for definition in definitions:
            FileHandler.write_lines(filepath, definition)


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
        1) If there is an exact match, show the definition(s) and save the
           query results into a file.
        2) If there is no exact match, but close matches exist, show the
           recommended words.
        3) If there is no exact match nor close matches, print no word found.
        """
        EXIT_COMMAND = "exitprogram"
        FILE_TO_SAVE = "result.txt"
        word = ""
        while word != EXIT_COMMAND:
            count = 0  # number of definitions.
            word = input("\nPlease type a word to search (Type 'exitprogram'"
                         " if you want to stop the program): ").lower()
            result = self.query_definition(word)
            close_words = get_close_matches(word, self.dictionary.keys())

            if word == EXIT_COMMAND:
                print("Bye!")
                return
            elif result is None and len(close_words) == 0:
                print("No word found.\n")
            elif result is not None:
                print(f"\n---------------------------------------------\n"
                      f"Query Results for [{word}]:")
                FileHandler.write_lines(FILE_TO_SAVE, f"\n{word}")
                for definition in result:
                    count += 1
                    definition = definition.replace('\\n', ' ')
                    print(f"{count}. {definition}")
                    FileHandler.write_lines(FILE_TO_SAVE,
                                            f"{count}. {definition}")
                print("----------------------------------------------")
            else:
                print(f"Were you looking for a word among {close_words} ?")


def main():
    """Instantiates Dictionary and runs the program."""

    my_dictionary = Dictionary()

    # Loads input file, and if loading was successful, runs the program.
    loaded = False
    INPUT_FILE = "data.json"
    try:
        my_dictionary.load_dictionary(INPUT_FILE)
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
        if loaded:
            my_dictionary.run_program()
        else:
            print("Failed to load the file.")


if __name__ == "__main__":
    main()
