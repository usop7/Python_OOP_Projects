import random
from datetime import datetime
from asteroid import Asteroid
from vector import Vector


class Controller:

    asteroid_list = []

    def __init__(self, n):
        i = 0
        while i < n:
            r = random.randint(1, 4)
            p = Vector(random.randint(0, 5), random.randint(0, 5), random.randint(0, 5))
            v = Vector(random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5))
            Controller.asteroid_list.append(Asteroid(r, p, v))
            i += 1

    def simulate(self, seconds):
        for asteroid in self.asteroid_list:
            i = 0
            while i < seconds:
                asteroid.move()


def main():
    Controller(5)


if __name__ == "__main__":
    main()
