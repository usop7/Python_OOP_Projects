from unittest import TestCase
from file_handler import FileHandler
from file_handler import InvalidFileTypeError


class TestFileHandler(TestCase):
    """
    Inherits from TestCase and is responsible for executing and housing
    the different unit tests for file_handler.py
    """
    def test_file_exists(self):
        """
        Unit test for load_data. Tests if the input file exists.
        :return:
        """
        self.assertRaises(FileNotFoundError, FileHandler.load_data, "abc.txt")

    def test_file_extension(self):
        """
        Unit test for load_data. Tests if a file is .txt or .json file.
        :return:
        """
        self.assertRaises(InvalidFileTypeError, FileHandler.load_data,
                          "dictionary.py")
