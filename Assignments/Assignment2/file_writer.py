"""This module holds classes that will be used for writing to files."""


class FileWriter:
    """This class holds methods that are used for writing to files."""

    @staticmethod
    def write_lines(path, lines):
        """
        It appends the given lines to a text file in the path.
        :param path: String
        :param lines: List of String
        """
        # Overwrites the file if the file exists.
        # If the file does not exist, creates a new file for writing.
        file = open(path, "w")
        for line in lines:
            file.write(f"{line}\n")
        file.close()
