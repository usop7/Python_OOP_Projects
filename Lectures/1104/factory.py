"""
This module depicts the factory pattern in action as it generates
different kinds of users for a hypothetical website.
"""
import enum
import abc
from datetime import  datetime


class Permission(enum.Enum):
    READ = 0,
    LIKE = 1,
    SHARE = 2,
    FLAG = 3,
    WRITE = 4


class User:

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.date_joined = datetime.now()
        self.permissions = None
        self.password = password

    def authenticate(self, password_input: str) -> bool:
        return password_input == self.password

    def get_profile(self) -> tuple:
        return self.username, self.date_joined

    def __str__(self):
        return f"Username: {self.username}, Date Joined: {self.date_joined}"


class Guest(User):

    def __init__(self, username: str, password: str) -> None:
        super().__init__(username, password)
        self.permissions = (Permission.READ, Permission.LIKE, Permission.SHARE,
                            Permission.FLAG)

    def __str__(self):
        return f"Guest User: {super().__str__()}"


class Member(User):

    def __init__(self, username:str, password: str) -> None:
        super().__init__(username, password)
        self.permissions = (Permission.READ, Permission.LIKE, Permission.SHARE,
                            Permission.FLAG, Permission.WRITE)

    def __str__(self):
        return f"Member User: {super().__str__()}"


# ---------  insert factory classes here ----------

class Forum:

    def __init__(self, name):
        self.name = name
        self.users = []
        self.registration_system = UserRegistrationSystem()

    def add_user(self):
        factory = self.registration_system.register_user()
        self.users.append(factory.create_user())


class UserRegistrationSystem:

    def __init__(self):
        self.choice_factory_mapping = {
            1: MemberUserFactory,
            2: GuestUserFactory
        }

    def register_user(self) -> UserFactory:
        print("Welcome! Do you want to make an account or continue as a guest?")
        print("1. Make Account")
        print("2. Continue as Guest")
        choice = int(input("Enter your choice (1-2)"))
        factory_class = self.choice_factory_mapping.get(choice, None)
        return factory_class()


def main():
    my_forum = Forum("Discussion Forum")
    my_forum.add_user()
    my_forum.add_user()
    for user in my_forum.users:
        print(user)


if __name__ == '__main__':
    main()