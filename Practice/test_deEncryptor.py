from unittest import TestCase
from question_a import DeEncryptor
from question_a import NoCharacterIntegerException

class TestDeEncryptor(TestCase):
    def test_convert_to_string(self):
        test_list = [72, 101, 108, 108, 111]
        encryptor = DeEncryptor()
        result = encryptor.convert_to_string(test_list)
        self.assertEqual(result, "Hello")

    def test_convert_to_string_type_error(self):
        test_list = ["t", 1]
        encryptor = DeEncryptor()
        self.assertRaises(TypeError, encryptor.convert_to_string, test_list)

    def test_convert_to_string_value_error(self):
        test_list = [1000]
        encryptor = DeEncryptor()
        self.assertRaises(NoCharacterIntegerException, encryptor.convert_to_string, test_list)




