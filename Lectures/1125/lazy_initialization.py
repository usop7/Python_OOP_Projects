import time
class Car:
    def __init__(self):
        print("Building a car. This is a time consuming process")
        time.sleep(2)
        print("Wait for it...")
        time.sleep(1)
        print("Car has been made")

    def __str__(self):
        return "I am an expensive car that uses a lot of resources"


class Client:

    def __init__(self):
        self._car = None

    @property
    def car(self) -> Car:
        if not self._car:
            self._car = Car()
        return self._car


def main():
    client = Client()
    print("I need a car")
    car = client.car


if __name__ == "__main__":
    main()