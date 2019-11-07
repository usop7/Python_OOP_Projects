class NoCharacterIntegerException(Exception):
    def __init__(self):
        super().__init__("Integer should be between 0 - 255.")

class DeEncryptor:

    def convert_to_string(self, integer_sequence):

        # check if all the numbers are valid ASCII characters
        for num in integer_sequence:
            if num < 0 or num > 255:
                raise NoCharacterIntegerException

        # convert it to character
        result = [chr(i) for i in integer_sequence]
        result_str = ""
        for c in result:
            result_str += c
        return result_str


def main():

    test_list = [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]
    encryptor = DeEncryptor()
    try:
        result = encryptor.convert_to_string(test_list)
    except TypeError as e:
        print("Error: The list can only take integers!!")
    except NoCharacterIntegerException as e:
        print(e)
    except Exception as e:
        print(f"Error: Unknown Exception occurred! {e}")
    else:
        print(result)


if __name__ == '__main__':
    main()
