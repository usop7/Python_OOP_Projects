import random
from datetime import datetime
import time
from asteroid import Asteroid
from vector import Vector


class Controller:
    """This class embodies the basic functions and attributes of a controller"""

    @classmethod
    def generate_vector(cls, max_):
        """
        Returns a Vector with random positions.
        :param max_: an int
        :return: a Vector object
        """
        return Vector(random.randint(-max_, max_), random.randint(-max_, max_), random.randint(-max_, max_))

    @classmethod
    def generate_radius(cls, min_radius, max_radius):
        """
        Returns a random integer between min_radius and max_radius.
        :param min_radius: an int
        :param max_radius: an int
        :return: an int
        """
        return random.randint(min_radius, max_radius)

    def __init__(self, cube_size, num_of_asteroid, min_radius, max_radius, max_velocity):
        """
        Initializes the cube size, number of asteroids, min/max radius of an asteroid, and max velocity of an asteroid.
        :param cube_size: an int
        :param num_of_asteroid: an int
        :param min_radius: an int
        :param max_radius: an int
        :param max_velocity: an int
        """
        self._asteroid_list = []
        # Creates n asteroids and add them to the asteroid list
        i = 0
        while i < num_of_asteroid:
            radius = Controller.generate_radius(min_radius, max_radius)
            position = Controller.generate_vector(cube_size)
            velocity = Controller.generate_vector(max_velocity)
            self._asteroid_list.append(Asteroid(radius, position, velocity))
            i += 1

    def simulate(self, seconds):
        """
        Moves every asteroid once per second for the number of seconds.
        The movement must starts precisely on the second.
        :param seconds: an int
        """
        micro_unit = 1000000
        i = 0
        while i < seconds:
            for asteroid in self._asteroid_list:
                asteroid.move()
                print(asteroid)
            time.sleep(1)
            i += 1
            print("--------------")


def main():
    """
    Creates a controller and simulates the asteroids' movements.
    """
    controller_a = Controller(100, 100, 1, 4, 5)
    controller_a.simulate(5)


if __name__ == "__main__":
    main()
