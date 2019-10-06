class BaseClass:

    def call_me(self):
        print("Base Class Method executed")


class LeftSubClass(BaseClass):

    def call_me(self):
        super().call_me()
        print("LeftSubClass Method executed")


class RightSubClass(BaseClass):

    def call_me(self):
        super().call_me()
        print("RightSubClass Method executed")


class ChildClass(LeftSubClass, RightSubClass):

    """
    Problematic
        def call_me(self):
        LeftSubClass.call_me(self)
        RightSubClass.call_me(self)
        print("ChildClass Method executed")
    """

    def call_me(self):
        super().call_me()
        print("ChildClass Method executed")


def main():
    test_object = ChildClass()
    test_object.call_me()


if __name__ == '__main__':
    main()
