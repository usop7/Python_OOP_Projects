def unpack(some_container):
    item1, item2, item3 = some_container
    print(item1)
    print(item2)
    print(item3)

unpack(("Hi", "There", "Michelle"))

"""
def __init__(age, name, **kwargs):
    print(age)
    print(name)
    print(kwargs)

__init__(name="Michelle", age=24, height="160cm")
"""


def __init__(age, name, **kwargs):
    print(age)
    print(name)
    super().__init__(name=name, age=age, **kwargs)

