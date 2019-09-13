class Vector:
    """This class embodies the basic functions and attributes of a vector"""

    def __init__(self, x, y, z):
        """
        Initialize the Vector x, y and z position.
        :param x: an int
        :param y: an int
        :param z: an int
        """
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        """
        Returns x.
        :return: an int
        """
        return self._x

    def get_y(self):
        """
        Returns y.
        :return: an int
        """
        return self._y

    def get_z(self):
        """
        Returns z.
        :return: an int
        """
        return self._z

    def set_x(self, x):
        """
        Sets x.
        :param x: an int
        """
        self._x = x

    def set_y(self, y):
        """
        Sets y.
        :param y: an int
        """
        self._y = y

    def set_z(self, z):
        """
        Sets z.
        :param z: an int
        """
        self._z = z

    x = property(get_x, set_x)
    y = property(get_y, set_y)
    z = property(get_z, set_z)

    def get_vector(self):
        """
        Returns the vector as a tuple.
        :return: a tuple
        """
        pos_vector = (self._x, self._y, self._z)
        return pos_vector

    def set_vector(self, vector):
        """
        Sets the x, y, and position of the vector.
        :param vector: Vector
        """
        self._x = vector.x
        self._y = vector.y
        self._z = vector.z

    vector = property(get_vector, set_vector)

    def add(self, vector):
        """
        Adds another vector to this vector and returns the new vector.
        :param vector: a Vector object
        :return: a Vector
        """
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z
        return self

    def __str__(self):
        """
        Returns the vector as a tuple.
        :returns a tuple
        """
        return self.vector


