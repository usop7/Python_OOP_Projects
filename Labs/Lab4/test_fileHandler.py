import os
from unittest import TestCase
from file_handler import FileHandler
from file_handler import InvalidFileTypeError


class TestFileHandler(TestCase):
    """
    Inherits from TestCase and is responsible for executing and housing
    the different unit tests for file_handler.py
    """
    def test_load_data_file_exists(self):
        """
        Unit test for load_data. Asserts that the function raises a
        FileNotFoundError if a provided file doesn't exist.
        """
        self.assertRaises(FileNotFoundError, FileHandler.load_data, "abc.txt")

    def test_load_data_file_extension(self):
        """
        Unit test for load_data. Asserts that the function raises a
        InvalidFileTypeError if a provided file is not json nor txt.
        """
        self.assertRaises(InvalidFileTypeError, FileHandler.load_data,
                          "dictionary.py")

    def test_load_data_function(self):
        """
        Unit test for load_data. Asserts that the function loads data
        and returns the loaded data properly.
        """
        loaded_data = FileHandler.load_data("test.txt")
        self.assertEqual(loaded_data, "test")

    def test_write_line(self):
        """
        Unit test for load_data. Asserts that the function creates a new
        file when there is no such file and appends the given line properly.
        """
        new_file = "output_text.txt"
        if os.path.exists(new_file):
            os.remove(new_file)
        line_to_write = "Hello Rahul!"
        FileHandler.write_lines(new_file, line_to_write)

        loaded_data = FileHandler.load_data(new_file)
        self.assertEqual(loaded_data, f"{line_to_write}\n")

