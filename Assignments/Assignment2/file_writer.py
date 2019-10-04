"""This module holds classes that will be used for writing to files."""


class FileWriter:
    """This class holds methods that are used for file handling."""

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

