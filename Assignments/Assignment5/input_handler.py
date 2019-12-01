"""
This module holds classes that will be used for reading
and writing to files.
"""

import argparse
from pathlib import Path
import os.path


import enum


class Mode(enum.Enum):
    """
    List the various query modes that the pokedex can search for.
    """
    POKEMON = "pokemon"
    ABILITY = "ability"
    MOVE = "move"
    STAT = "stat"

    @staticmethod
    def is_valid_mode(mode: str):
        """
        Check if the query mode is among {pokemon, ability, or move}
        and return true. If not, raise an exception.
        :param mode: String
        :return: bool
        """
        valid = [Mode.POKEMON.value, Mode.ABILITY.value, Mode.MOVE.value]
        if mode.lower() not in valid:
            raise ValueError("Invalid query mode.")
        return True


class Request:
    """
    The request object represents a request to get a data from the API.
    The request object comes with certain accompanying configuration options:
     - mode: Mode enum
     - param: list of str
     - expanded: boolean
     - output: 'filename.txt' or 'print' by default
    """

    def __init__(self, mode: Mode, params: list, expanded: bool,
                 output: str = "print"):
        self.mode = mode
        self.params = params
        self.expanded = expanded
        self.output = output

    def __str__(self):
        return f"\n{'='*29} Request Summary {'='*29}\n" \
               f"\nMode: {self.mode.value}" \
               f"\nInput Value: {self.params}" \
               f"\nExpanded: {self.expanded}" \
               f"\nOutput: {self.output}\n"


class IOHandler:
    """This class holds methods that are used for input handling."""

    @staticmethod
    def is_txt_file(path: str) -> bool:
        """Return true if the given file path ends with '.txt'"""
        return Path(path).suffix == ".txt"

    @staticmethod
    def load_input(input_value: str) -> list:
        """
        Read an input value and append it to a list and return it.
        Input value can be the given parameter itself or read from the file.

        1. If an input value ends with '.txt' check if the file path exists,
          if not, raise an exception.
          Then, read lines in the file and append them to a list.
        2. If an input value doesn't end with '.txt' append it to a list.

        Then return the list.
        :param input_value: String
        :return: list of string
        """
        data = []
        if IOHandler.is_txt_file(input_value):
            if not os.path.exists(input_value):
                raise FileNotFoundError("File not found!")
            else:
                with open(input_value, mode='r', encoding='utf-8') as file:
                    data = [line.strip().lower() for line in file]
        else:
            data.append(input_value)
        return data

    @staticmethod
    def validate_output_arg(output: str) -> bool:
        """
        Check if output argument ends with '.txt' extension, and return True.
        If not, raise an exception.
        :param output:
        :return:
        """
        if output != "print" and not IOHandler.is_txt_file(output):
            raise ValueError("Output file must end with '.txt'")
        return True

    @staticmethod
    def write_data(path: str, data: str):
        """
        It writes the given data to a text file in the path.
        If the file doesn't exist, create it.
        :param path: String
        :param data: String
        """
        # Open a file for writing and create if it doesn't exist.
        with open(path, mode='w+', encoding='utf-8') as file:
            file.write(data)

    @staticmethod
    def setup_request_commandline() -> Request:
        """
        Implements the argparse module to accept arguments via the command
        line. This function specifies what these arguments are and parses it
        into an object of type Request. If something goes wrong with
        provided arguments then the function prints an error message and
        exits the application.
        :return: The object of type Request with all the arguments provided
        in it.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("mode", type=str.lower,
                            help="The mode specifies which information to "
                                 "query. This needs to be among the following:"
                                 " {pokemon | ability | move}")
        parser.add_argument("input",
                            help="The id or name that you want to search for. "
                                 "Or it can be set to a file name that ends "
                                 "with '.txt' as well. "
                                 "{filename.txt | name or id}")
        parser.add_argument("--expanded", action="store_true",
                            help="With the expanded flag, pokedex will query "
                                 "more information. It only applies to"
                                 " 'pokemon' mode.")
        parser.add_argument("--output", default="print",
                            help="The output represents the way you want to "
                                 "get the query result. It is 'print' by "
                                 "default but you can specify a file name. "
                                 "In that case, the file must end with '.txt'")
        try:
            args = parser.parse_args()

            # check the mode's validity
            Mode.is_valid_mode(args.mode)

            # convert input data into a list
            input_data = IOHandler.load_input(args.input)

            # check if the output file (if specified) ends with '.txt'.
            IOHandler.validate_output_arg(args.output)

            # create a Request object
            request = Request(Mode(args.mode), input_data,
                              args.expanded, args.output)
            print(request)
            return request
        except Exception as e:
            print(f"Error! Please check your request arguments!\n{e}")
            quit()

