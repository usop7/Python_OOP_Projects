from des import DesKey
import argparse
import abc
import enum
import os.path
import ast


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
        - data: This is the data to be encrypted or decrypted, either from
        data_input or input_file.

    """
    def __init__(self, output="print", encryption_state="en"):
        self.encryption_state = encryption_state
        self.data_input = None
        self.input_file = None
        self.output = output
        self.key = None
        self.result = None
        self.data = None

    def __str__(self):
        return f"Request: State: {self.encryption_state}, Data: {self.data}" \
               f", Input file: {self.input_file}, " \
               f"Data Input: {self.data_input} Output: {self.output}, " \
               f"Key: {self.key}\n"


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
                        help="The mode to run the program in. If 'en'(default)"
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

        # Handler Chains for Encryption
        key_handler = ValidateKeyHandler()
        mode_handler = ValidateModeHandler()
        input_source_handler = InputSourceHandler()
        populate_data_handler = PopulateDataHandler()
        input_data_handler = ValidateInputDataHandler()
        encrypt_handler = EncryptDataHandler()
        output_handler = OutputHandler()

        key_handler.set_next_handler(mode_handler)
        mode_handler.set_next_handler(input_source_handler)
        input_source_handler.set_next_handler(populate_data_handler)
        populate_data_handler.set_next_handler(input_data_handler)
        input_data_handler.set_next_handler(encrypt_handler)
        encrypt_handler.set_next_handler(output_handler)

        # Handler Chains for Decryption
        key_handler2 = ValidateKeyHandler()
        mode_handler2 = ValidateModeHandler()
        input_source_handler2 = InputSourceHandler()
        populate_data_handler2 = PopulateDataHandler()
        input_data_handler2 = ValidateInputDataHandler()
        decrypt_handler = DecryptDataHandler()
        output_handler2 = OutputHandler()

        key_handler2.set_next_handler(mode_handler2)
        mode_handler2.set_next_handler(input_source_handler2)
        input_source_handler2.set_next_handler(populate_data_handler2)
        populate_data_handler2.set_next_handler(input_data_handler2)
        input_data_handler2.set_next_handler(decrypt_handler)
        decrypt_handler.set_next_handler(output_handler2)

        self.encryption_start_handler = key_handler
        self.decryption_start_handler = key_handler2

    def execute_request(self, request: Request):

        if request.encryption_state == CryptoMode.EN.value:
            result = self.encryption_start_handler.handle_request(request)
        else:
            result = self.decryption_start_handler.handle_request(request)

        if result[0]:
            return True
        else:
            print(result[1])
            return False


class BaseDesHandler(abc.ABC):
    """
    Baseclass for all handlers that handle Encryption and Decryption Request.
    Each concrete handler will be inherited from this BaseHandler.
    """

    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abc.abstractmethod
    def handle_request(self, command: Request) -> (bool, str):
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

    def pass_handler(self, command):
        """
        :param command: a Request
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the form or not.
        """
        if not self.next_handler:
            return True, ""
        return self.next_handler.handle_request(command)


class ValidateKeyHandler(BaseDesHandler):
    """
    This handler ensures that the Key exists and is a length of 8, 16 or 24.
    """

    def handle_request(self, command: Request) -> (bool, str):
        """
        Check if the length of the key value is either 8, 16 or 24.
        :param command: a Request
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the form or not.
        """
        if len(command.key) not in [8, 16, 24]:
            return False, "The Key needs to be of length 8, 16 or 24"

        return self.pass_handler(command)


class ValidateModeHandler(BaseDesHandler):
    """
    This handler ensures that a mode belongs to the CryptoMode..
    """

    def handle_request(self, command: Request) -> (bool, str):
        """
        Check if a mode matches any value of CryptoMode Enum type's value.
        :param command: a Request
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the form or not.
        """
        print("Validating Mode")
        mode = command.encryption_state
        found = False
        for mode_type in CryptoMode:
            if mode_type.value == mode:
                found = True
        if not found:
            return False, "Mode not found."

        return self.pass_handler(command)


class InputSourceHandler(BaseDesHandler):
    """
    This handler ensures that the request has an input data, either
    a String or an input file.
    """

    def handle_request(self, command: Request) -> (bool, str):
        """
        Check if an input source exists, either input file or data input.
        :param command: a Request
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the form or not.
        """
        print("Validating input data source")
        str_data = command.data_input
        file_data = command.input_file
        if str_data is None and file_data is None:
            return False, "No input data found."
        if str_data is not None and file_data is not None:
            return False, "Please specify only one input source."
        return self.pass_handler(command)


class PopulateDataHandler(BaseDesHandler):
    """
    It populates data attribute of request with data source.
    """

    def handle_request(self, command: Request) -> (bool, str):
        """
        If it is a file, check if the file exists and read/copy the data
        from the file.
        If it is a string, copy the data.
        :param command: a Request
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the form or not.
        """
        print("Validating input data file")
        file_path = command.input_file
        if file_path is not None:
            if not os.path.exists(file_path):
                return False, "Input file doesn't exist."
            else:
                mode = 'r' if command.encryption_state == 'en' else 'rb'
                with open(file_path, mode=mode) as file:
                    command.data = file.read()
        else:
            command.data = command.data_input
        return self.pass_handler(command)


class ValidateInputDataHandler(BaseDesHandler):
    """
    It ensures that the data is a right type and not emtpy.
    """

    def handle_request(self, command: Request) -> (bool, str):
        """
        It checks if the request's data is right type (bytes or string),
        and not empty.
        :param command: a Request
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the form or not.
        """

        print("Validating input data type and emptiness")
        if command.encryption_state == 'de':
            command.data = ast.literal_eval(command.data)
            if not isinstance(command.data, bytes):
                return False, "Input data is not byte type"
        if command.data == "":
            return False, "The input data is empty."
        return self.pass_handler(command)


class EncryptDataHandler(BaseDesHandler):
    """It encrypts the data."""

    def handle_request(self, command: Request) -> (bool, str):
        """
        It converts the Key into DesKey and encrypt the data,
        assigns it to a result attribute of the request.
        :param command: a Request
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the form or not.
        """

        print("Encrypting...")
        key = DesKey(command.key.encode("utf-8"))
        command.result = key.encrypt(command.data.encode("utf-8"), padding=True)
        return self.pass_handler(command)


class DecryptDataHandler(BaseDesHandler):
    """It decrypts the data."""

    def handle_request(self, command: Request) -> (bool, str):
        """
        It conveerts the Key into DesKey and decrypt the data,
        assigns it to a result attribute of the request.
        :param command: a Request
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the form or not.
        """
        print("Decrypting...")
        try:
            key = DesKey(command.key.encode("utf-8"))
            command.result = key.decrypt(command.data, padding=True).decode("utf-8")
        except Exception as e:
            return False, f"Decryption Failed!"
        else:
            return self.pass_handler(command)


class OutputHandler(BaseDesHandler):

    def handle_request(self, command: Request) -> (bool, str):
        """
        It
        :param command:
        :return:
        """
        print("Generating results")
        if command.output.lower() != "print":
            mode = 'wb' if command.encryption_state == 'en' else 'w'
            with open(command.output, mode) as file:
                file.write(command.result)
        else:
            print(command.result)
        return self.pass_handler(command)


def main(request: Request):
    crypto_system = Crypto()
    crypto_system.execute_request(request)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
