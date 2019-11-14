import des
import argparse
import abc
import enum
import os.path


class CryptoMode(enum.Enum):
    """
    Lists the various modes that the Crypto application can run in.
    """
    # Encryption mode
    EN = "en"
    # Decryption Mode
    DE = "de"


class Request:
    """
    The request object represents a request to either encrypt or decrypt
    certain data. The request object comes with certain accompanying
    configuration options as well as a field that holds the result. The
    attributes are:
        - encryption_state: 'en' for encrypt, 'de' for decrypt
        - data_input: This is the string data that needs to be encrypted or
        decrypted. This is None if the data is coming in from a file.
        - input_file: The text file that contains the string to be encrypted or
        decrypted. This is None if the data is not coming from a file and is
        provided directly.
        - output: This is the method of output that is requested. At this
        moment the program supports printing to the console or writing to
        another text file.
        - key: The Key value to use for encryption or decryption.
        - result: Placeholder value to hold the result of the encryption or
        decryption. This does not usually come in with the request.

    """
    def __init__(self):
        self.encryption_state = None
        self.data_input = None
        self.input_file = None
        self.output = None
        self.key = None
        self.result = None

    def __str__(self):
        return f"Request: State: {self.encryption_state}, Data: {self.data_input}" \
               f", Input file: {self.input_file}, Output: {self.output}, " \
               f"Key: {self.key}"


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="The key to use when encrypting or "
                                    "decrypting. This needs to be of "
                                    "length 8, 16 or 24")
    parser.add_argument("-s", "--string", help="The string that needs to be "
                                               "encrypted or decrypted")
    parser.add_argument("-f", "--file", help="The text file that needs to be"
                                             "encrypted or decrypted")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")
    parser.add_argument("-m", "--mode", default="en",
                        help="The mode to run the program in. If 'en' (default)"
                             " then the program will encrypt, 'de' will cause "
                             "the program to decrypt")
    try:
        args = parser.parse_args()
        request = Request()
        request.encryption_state = args.mode
        request.data_input = args.string
        request.input_file = args.file
        request.output = args.output
        request.key = args.key
        print(request)
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


class Crypto:

    def __init__(self):
        """
        Set up the Crypto program and create a chain of handlers.
        """

        key_handler = ValidateKeyHandler()
        input_handler = InputDataHandler()
        file_handler = InputFileHandler()
        mode_handler = ValidateModeHandler()

        key_handler.set_next_handler(input_handler)
        input_handler.set_next_handler(mode_handler)
        mode_handler.set_next_handler(file_handler)

        self.encryption_start_handler = key_handler
        self.decryption_start_handler = key_handler

    def execute_request(self, request: Request):
        result = self.encryption_start_handler.handle_request(request)

        if result[0]:
            mode = result[1]
            data = result[2]
            print(mode)
            print(data)
            return False
        else:
            print(result[2])
            return False


class BaseDesHandler(abc.ABC):
    """
    Baseclass for all handlers that handle Encryption and Decryption Request.
    Each concrete handler will be inherited from this BaseHandler.
    """

    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abc.abstractmethod
    def handle_request(self, command: Request) -> (bool, str, CryptoMode):
        """
        Each Handler will have a specific implementation of how it processes
        a request.
        :param command: a Request
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the form or not.
        """
        pass

    def set_next_handler(self, handler):
        self.next_handler = handler


class ValidateKeyHandler(BaseDesHandler):
    """
    This handler ensures that the Key exists and is a length of 8, 16 or 24.
    """

    def handle_request(self, command: Request) -> (bool, str, CryptoMode):
        """
        Check if the length of the key value is either 8, 16 or 24.
        :param command: a Request
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the form or not.
        """
        if command.key is None:
            return False, None, "The Key is required."
        if len(command.key) not in [8, 16, 24]:
            return None, "The Key value needs to be of length 8, 16 or 24", False

        if not self.next_handler:
            return True, command.encryption_state, command.data_input
        return self.next_handler.handle_request(command)


class ValidateModeHandler(BaseDesHandler):
    """
    This handler ensures that a mode belongs to the CryptoMode..
    """

    def handle_request(self, command: Request) -> (bool, str, CryptoMode):
        """
        Check if a mode matches any value of CryptoMode Enum type's value.
        :param command: a Request
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the form or not.
        """
        mode = command.encryption_state
        found = False
        for mode_type in CryptoMode:
            if mode_type.value == mode:
                found = True
        if not found:
            return False, None, "Mode not found."

        if not self.next_handler:
            return True, command.encryption_state, command.data_input
        return self.next_handler.handle_request(command)


class InputDataHandler(BaseDesHandler):
    """
    This handler ensures that the request has an input data, either
    a String or an input file.
    """

    def handle_request(self, command: Request) -> (bool, str, CryptoMode):
        """
        Check if an input data exists, either input file or data input.
        :param command: a Request
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the form or not.
        """
        print("Validating input data")
        str_data = request.data_input
        file_data = request.input_file
        if str_data is None and file_data is None:
            return None, "No input data found.", False

        if not self.next_handler:
            return True, command.encryption_state, command.data_input
        return self.next_handler.handle_request(command)


class InputFileHandler(BaseDesHandler):
    """
    This handler ensures that the input data file exists.
    """

    def handle_request(self, command: Request) -> (bool, str, CryptoMode):
        """
        Check if there exists a given file, and if it has a contents.
        :param command: a Request
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the form or not.
        """
        print("Validating input file")
        file_path = request.input_file
        input_str = request.data_input
        data = None
        if file_path is not None:
            if not os.path.exists(file_path):
                return False, None, "Input file doesn't exist."
            else:
                with open(file_path, mode='r', encoding='utf-8') as file:
                    data = file.read()
        else:
            data = input_str

        if data == "":
            return False, None, "Input file doesn't have any content in it."

        if not self.next_handler:
            return True, command.encryption_state, data
        return self.next_handler.handle_request(command)


def main(request: Request):
    crypto_system = Crypto()
    crypto_system.execute_request(request)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
