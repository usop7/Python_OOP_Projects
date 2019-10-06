class Base1:
    pass


class Base2:
    pass


class MultiDerived (Base2, Base1):
    pass


print(MultiDerived.mro())
