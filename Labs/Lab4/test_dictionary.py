from unittest import TestCase
from dictionary import Dictionary
from dictionary import WordNotFoundException


class TestDictionary(TestCase):
    """
    Inherits from TestCase and is responsible for executing and housing
    the different unit tests for dictionary.py
    """

    @classmethod
    def create_dictionary_obj(cls):
        """
        Creates a dictionary object, and loads the file into it.
        :return: Dictionary
        """
        my_dictionary = Dictionary()
        my_dictionary.load_dictionary("data.json")
        return my_dictionary

    def test_load_dictionary_valid_file(self):
        """
        Unit test for load_data. Asserts that the functions returs true
        if the input file is a valid json file.
        """
        my_dictionary = TestDictionary.create_dictionary_obj()
        self.assertTrue(my_dictionary.load_dictionary("data.json"))

    def test_query_definition_found(self):
        """
        Unit test for query_definition. Tests if it returns true if if
        finds a word in a given dictionary.
        """
        my_dictionary = TestDictionary.create_dictionary_obj()
        self.assertTrue(my_dictionary.query_definition("dog"))

    def test_query_definition_not_found(self):
        """
        Unit test for query_question. Asserts that the function raises a
        WordNotFoundException if it doesn't find a word.
        """
        my_dictionary = TestDictionary.create_dictionary_obj()
        self.assertRaises(WordNotFoundException,
                          my_dictionary.query_definition, "leeseul kim")

