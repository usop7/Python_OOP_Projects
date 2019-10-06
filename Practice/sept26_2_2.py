class BaseClass:

    def call_me(self, name='', age=0):
        print(f"Base Class Method executed name: {name}\t age: {age}")


class LeftSubClass(BaseClass):

    def call_me(self, age=0, **kwargs):
        super().call_me(**kwargs)
        print(f"LeftSubClass Method executed age: {age}")


class RightSubClass(BaseClass):

    def call_me(self, weight='', **kwargs):
        super().call_me(**kwargs)
        print(f"RightSubClass Method executed Weight: {weight}")


class ChildClass(LeftSubClass, RightSubClass):

    """
    Problematic
        def call_me(self):
        LeftSubClass.call_me(self)
        RightSubClass.call_me(self)
        print("ChildClass Method executed")
    """

    def call_me(self, height="", **kwargs):
        super().call_me(**kwargs)
        print(f"ChildClass Method executed Height: {height}")


def main():
    test_object = ChildClass()
    test_object.call_me(name="Leeseul", age=99, weight=80, height=140)


if __name__ == '__main__':
    main()
