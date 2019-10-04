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

    def test_write_line(self):
        """
        Unit test for load_data. Asserts that the function creates a new
        file when there is no such file and appends the given line properly.
        """
        # Writes a line
        new_file = "output_text.txt"
        if os.path.exists(new_file):
            os.remove(new_file)
        line_to_write = "Hello Rahul!"
        FileHandler.write_lines(new_file, line_to_write)

        # Open the newly created file and read
        file = open(new_file, mode='r', encoding='utf-8')
        result = file.read()
        file.close()

        # Asserts two strings are the same
        self.assertEqual(result, f"{line_to_write}\n")

