from abc import ABC, abstractmethod


class Mediator(ABC):
    """
    All Mediators must implement a common interface so that all the
    other components that communicate via the Mediator can talk to it.
    """
    @staticmethod
    def notify(sender, **kwargs):
        pass


class Button:
    """
    A re-usable button component. This can be used in any screen and
    just needs a reference to Mediator to work.
    """

    def __init__(self, mediator: Mediator):
        self.mediator = mediator

    def on_click(self):
        self.mediator.notify(self)


class InputField:
    """
    An input field that allows user to enter some data. This can be
    reused in any screen and just needs a reference to a Mediator to
    work.
    """

    def __init__(self, mediator: Mediator):
        self.mediator = mediator
        self.text = ""

    def enter_data(self):
        self.text = input("Enter text: ")
        self.mediator.notify(self, input_txt=self.text)


class TextLabel:
    """
    Displays a line of text. You can have this class reference a
    mediator to keep things consistent and you probably would have to in
    a more complex system, but I chose not to because it would never use
    it.
    """

    def __init__(self):
        self.text = None

    def display_text(self, prefix):
        """
        Display text if it is initalized.
        :param prefix: a str, a prefex tag
        """
        if self.text:
            print(f"{prefix}: {self.text}")


class LoginMediator(Mediator):
    """
    The Login Mediator is responsible for handling any and all communication
    between all the components that make up a log in screen. In this case, to
    keep things simple it also has the added responsibility of driving the
    log in screen execution. This isn't mandatory.
    """

    def __init__(self):
        """
        Initialize the log in screen components and some test data.
        All components have a reference to the mediator.
        """
        self.credentials_db = {}
        self.credentials_db["jojoBeans"] = "passw0rdZ"
        self.credentials_db["zorak_the_destroyer"] = "i_am_l33t"
        self.status_text = TextLabel()
        self.user_inputfield = InputField(self)
        self.password_inputfield = InputField(self)
        self.login_btn = Button(self)
        self.exit_btn = Button(self)
        self.exit_screen = False

    def execute(self):
        """
        Execution loop for accepting user input and simulating a log in screen
        UI.
        """
        input_map = {
            1: self.user_inputfield.enter_data,
            2: self.password_inputfield.enter_data,
            3: self.login_btn.on_click,
            4: self.exit_btn.on_click
        }
        while not self.exit_screen:
            print("Welcome!")
            print("\nLogin Screen")
            print("-" * 30)
            self.status_text.display_text("Status")
            print("Username: ", self.user_inputfield.text)
            password = "*" * len(self.password_inputfield.text)
            # password = ''.join(password)
            print("Password: ", password)

            print("\n")
            print("--------------\t\t------------")
            print("|Login Button|\t\t|ExitButton|")
            print("--------------\t\t------------")

            print("\nWhat do you want to do?")
            print("1.Enter Username")
            print("2.Enter Password")
            print("3.Press the Login Button")
            print("4.Press the Exit Button")
            try:
                choice = int(input())
                input_map[choice]()
            except Exception:
                print("Invalid input!")

    def notify(self, sender, **kwargs):
        """
        This method is responsible for handling communication between all the
        log in components and facilitating any events triggered (Eg: on click).
        :param sender: an object, a log in screen component
        :param kwargs: optional parameters needed to facilitate event.
        """
        if sender == self.exit_btn:
            self.exit_screen = True
        elif sender == self.user_inputfield:
            if kwargs["input_text"] != "" and kwargs["input_text"] in self.credentials_db:
                self.status_text.text = "Username does not exist."
        elif sender == self.login_btn:
            if self.user_inputfield:
                self.status_text.text = "Log in Failed! Combination is incorrect"
        # exit btn
        # username input field
        # login button
        pass


def main():
    login__mediator = LoginMediator()
    login__mediator.execute()


if __name__ == '__main__':
    main()