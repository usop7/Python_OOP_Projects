"""This module holds classes that will be used for user input handling."""


class NoCheeseAddedException(Exception):
    """This exception will be raised when there is no cheese added."""
    def __init__(self):
        super().__init__("\n[Error] Please select at least one cheese!")


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

    @staticmethod
    def prompt_menu(question, option_list):
        """
        Prompt user with a list of options, and returns the selected option.
        The 'skip' option will be added to the end of the given list.
        :param question: String
        :param option_list: list
        :return: None or an Item in the list
        """
        while True:
            answer = input(question)
            # When choose to 'skip'(last option)
            if answer == str(len(option_list) + 1):
                return None
            else:
                try:
                    InputHandler.validate(len(option_list), answer)
                except ValueError:
                    print("\n[Error] Please type an integer!")
                except CommandNotFoundException as e:
                    print(f"{e}")
                else:
                    return option_list[int(answer) - 1]
