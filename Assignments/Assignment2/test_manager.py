"""This module is to test card app's major features."""
from unittest import TestCase
from unittest.mock import patch
from app import Manager
import os
from datetime import datetime


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

    def test_backup_card_list(self):
        """
        Unit test for backup_card_list. Asserts that the function creates a
        new file named CardManager_Export_DDMMYYYY_HHMM.txt.
        """
        file_exist = False

        # back up file
        m = Manager()
        m.backup_card_list()

        # check if the corresponding file has been created.
        now = datetime.now()
        path = f"CardManager_Export_{now.strftime('%d%m%Y_%H%M')}.txt"
        if os.path.exists(path):
            file_exist = True
        self.assertTrue(file_exist)






