"""This module holds classes that will be used for reading
and writing to files."""

from enum import Enum
from pathlib import Path
import os.path


class FileExtensions(Enum):
    """This class represents a file extension."""
    TXT = ".txt"
    JSON = ".json"


class FileHandler:
    """This class holds methods that are used for file handling."""

    @staticmethod
    def load_data(path):
        """
        Read a file in the path, and returns the String data.
        :param path: String
        :return: String
        """
        extension = Path(path).suffix
        if not os.path.exists(path):
            raise FileNotFoundError(f"file named {path} doesn't exists.")
        if extension != FileExtensions.TXT.value and extension != FileExtensions.JSON.value:
            raise TypeError("Only txt/json files are acceptable!")

        text_file = open(path, mode='r', encoding='utf-8')
        data = text_file.read()
        return data

    @staticmethod
    def write_lines(path, lines):
        """
        It appends the given lines to a text file in the path.
        :param path: String
        :param lines: String
        """

        # Open a file for writing and create if it doesn't exist.
        file = open(path, "a+")

        # Append the given lines to the file.
        file.write(f"{lines}\n")
        file.close()



