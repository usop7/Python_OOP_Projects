from datetime import datetime


class Asteroid:
    """This class embodies the basic functions and attributes of an asteroid."""

    # Each asteroid has a sequential unique ID starting from 1.
    id = 1

    @classmethod
    def increase_id(cls):
        """
        Increases id by 1.
        """
        cls.id += 1

    def __init__(self, radius, position, velocity):
        """
        Initializes an asteroid's radius, position and velocity.
        :param radius: an int
        :param position: a Vector object
        :param velocity: a Vector object
        """
        self._id = Asteroid.id
        self._radius = radius
        self._position = position
        self._velocity = velocity
        self._timestamp = datetime.now()
        Asteroid.increase_id()

    def get_position(self):
        """
        Returns the position.
        :return: a Vector object
        """
        return self._position

    def get_velocity(self):
        """
        Returns the velocity.
        :return: a Vector object
        """
        return self._velocity

    def set_position(self, position):
        """
        Sets the position.
        :param position: a Vector object
        """
        self._position = position

    def set_velocity(self, velocity):
        """
        Sets the velocity.
        :param velocity: a Vector object.
        """
        self._velocity = velocity

    position = property(get_position, set_position)
    velocity = property(get_velocity, set_velocity)

    def __str__(self):
        """
        :return: A user friendly formatted string depicting the asteroid attribute.
        """
        return f"ID: {self._id}, radius: {self._radius}, position: {self._position.__str__()}, velocity: {self._velocity.__str__()}, timestamp: {self._timestamp}"

    def move(self):
        """
        Modifies the position using the  velocity and returns the new position.
        :return: a tuple of x,y and z
        """
        new_position = self.position.add(self.velocity)
        self.position = new_position
        return new_position.vector
