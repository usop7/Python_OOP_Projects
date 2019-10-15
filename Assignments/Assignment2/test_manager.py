"""This module is to test card app's major features."""
from unittest import TestCase
from unittest.mock import patch
from app import Manager


class TestManager(TestCase):
    """
    Inherits from TestCase and is responsible for executing and housing
    the different unit tests for app.py.
    """

    def setUp(self):
        self.m = Manager()

    @patch('builtins.input')
    def test_add_card(self, m_input):
        """
        Unit test for add_card. Asserts that the method creates a card
        based on multiple user inputs.
        """
        m = Manager()
        m_input.side_effect = ["1", "BCIT", "A01029289",
                               "Leeseul Kim", "2020-05-01", ""]
        m.add_card()
        self.assertEqual(len(m._card_list), 1)

    @patch('builtins.input')
    def test_search_card(self, m_input):
        """
        Unit test for search_card. Asserts that the method returns True
        after searching for the card 'BCIT'.
        """
        m = Manager()
        m_input.side_effect = ["1", "BCIT", "A01029289",
                               "Leeseul Kim", "2020-05-01", ""]
        m.add_card()

        m_input.side_effect = ["BCIT"]
        self.assertTrue(m.search_card())



