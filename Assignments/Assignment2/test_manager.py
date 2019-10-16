"""This module is to test card app's major features."""
from unittest import TestCase
from unittest.mock import patch
from app import Manager


class TestManager(TestCase):
    """
    Inherits from TestCase and is responsible for executing and housing
    the different unit tests for app.py.
    """

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

    @patch('builtins.input')
    def test_delete_card_by_id(self, m_input):
        """
        Unit test for delete_card_by_id. Asserts the method returns True
        after deleting a card whose id is 2.
        """
        m = Manager()
        m_input.side_effect = ["1", "BCIT", "A01029289",
                               "Leeseul Kim", "2020-05-01", ""]
        m.add_card()
        m_input.side_effect = ["2"]
        self.assertTrue(m.delete_card_by_id())

    @patch('builtins.input')
    def test_delete_card_by_name(self, m_input):
        """
        Unit test for delete_card_by_name. Asserts the method returns True
        after deleting a card whose name is BCIT.
        """
        m = Manager()
        m_input.side_effect = ["1", "BCIT", "A01029289",
                               "Leeseul Kim", "2020-05-01", ""]
        m.add_card()
        m_input.side_effect = ["BCIT"]
        self.assertTrue(m.delete_card_by_name())






