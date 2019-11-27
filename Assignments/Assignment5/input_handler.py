"""
This module holds classes that will be used for reading
and writing to files.
"""

from pathlib import Path
import os.path


class FileHandler:
    """This class holds methods that are used for file handling."""

    @staticmethod
    def load_input(input_value):
        """
        Read a file in the path, and converts it to dictionary and return it.
        It will throw an exception in the following cases:
        1) The file does not exists.
        2) The file is not txt file.
        :param input_value: String
        :return: String
        """
        data = []
        if Path(input_value).suffix == ".txt":
            if not os.path.exists(input_value):
                raise FileNotFoundError("File not found!")
            else:
                with open(input_value, mode='r', encoding='utf-8') as file:
                    for line in file:
                        data.append(line.strip())
        else:
            data.append(input_value)
        return data

    @staticmethod
    def write_lines(path, lines):
        """
        It appends the given lines to a text file in the path.
        :param path: String
        :param lines: String
        """
        # Open a file for writing and create if it doesn't exist.
        file = open(path, "w+")

        # Append the given lines to the file.
        file.write(f"{lines}\n")
        file.close()

