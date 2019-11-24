import os.path

class InputHandler:

    @staticmethod
    def validate_int(value):
        """
        If a given value is not an int, raise an exception.
        :param value: int
        """
        if isinstance(value, str):
            raise ValueError("[Error] Please check the input data type.")

    @staticmethod
    def validate_file(file_path):
        """
        If the given file path doesn't exist, raise an exception
        :param file_path:
        :return:
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError("[Error] File not found!")
