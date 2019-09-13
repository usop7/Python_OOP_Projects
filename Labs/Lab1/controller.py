import random
from datetime import datetime
import time
from asteroid import Asteroid
from vector import Vector


class Controller:

    def __init__(self, n):
        self._asteroid_list = []
        i = 0
        while i < n:
            r = random.randint(1, 4)
            p = Vector(random.randint(0, 5), random.randint(0, 5), random.randint(0, 5))
            v = Vector(random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5))
            self._asteroid_list.append(Asteroid(r, p, v))
            i += 1

    def simulate(self, seconds):
        i = 0
        while i < seconds:
            if datetime.now().microsecond < 100:
                for asteroid in self._asteroid_list:
                    asteroid.move()
                    print(asteroid)
                time.sleep(1)
                i += 1
                print("--------------")


def main():
    c = Controller(2)
    c.simulate(5)


if __name__ == "__main__":
    main()
