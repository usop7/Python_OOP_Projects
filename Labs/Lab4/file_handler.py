"""This module holds classes that will be used for reading
and writing to files."""

from enum import Enum
from pathlib import Path
import os.path


class FileExtensions(Enum):
    """This class holds valid file extensions."""
    TXT = ".txt"
    JSON = ".json"

    @classmethod
    def is_valid_extension(cls, value):
        """
        Returns if the given value is in the enum list.
        :param value: String
        :return: boolean
        """
        return value in cls._value2member_map_


class FileHandler:
    """This class holds methods that are used for file handling."""

    @staticmethod
    def load_data(path):
        """
        Read a file in the path, and returns the String data.
        It will throw an exception in the following cases:
        1) The file does not exists.
        2) The file is not json nor txt file.
        :param path: String
        :return: String
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f"A file named {path} doesn't exists.")
        if FileExtensions.is_valid_extension(Path(path).suffix):
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



