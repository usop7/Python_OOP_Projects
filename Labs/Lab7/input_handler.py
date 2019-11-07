"""This module holds classes that will be used for user input handling."""

class CommandNotFoundException(Exception):
    """This exception will be raised when the input value is not valid."""
    def __init__(self, num):
        super().__init__(f"\n[Error] Please select between 1 to {num}")


class InputHandler:
    """This class holds methods that are used for user input handling."""

    @staticmethod
    def validate(num_commands, user_input):
        """
        If user input is not valid, raises a corresponding error.
        1. If user input is not digit, raises ValueError
        2. If user input is not between a proper range, raises an error.
        :param num_commands: int
        :param user_input: String
        """
        if not user_input.isdigit():
            raise ValueError
        if int(user_input) < 1 or int(user_input) > num_commands:
            raise CommandNotFoundException(num_commands)