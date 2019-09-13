from datetime import datetime


class Asteroid:

    id = 1

    @classmethod
    def increase_id(cls):
        cls.id += 1

    def __init__(self, radius, position, velocity):
        self._id = Asteroid.id
        self._radius = radius
        self._position = position
        self._velocity = velocity
        self._timestamp = datetime.now()
        Asteroid.increase_id()

    def get_radius(self):
        return self._radius

    def get_position(self):
        return self._position

    def get_velocity(self):
        return self._velocity

    def get_timestamp(self):
        return self._timestamp;

    def set_radius(self, radius):
        self._radius = radius

    def set_position(self, position):
        self._position = position

    def set_velocity(self, velocity):
        self._velocity = velocity

    def set_timestamp(self, timestamp):
        self._timestamp = timestamp

    def __str__(self):
        return f"ID: {self._id}, radius: {self._radius}, position: {self._position.__str__()}, velocity: {self._velocity.__str__()}, timestamp: {self._timestamp}"

    radius = property(get_radius, set_radius)
    position = property(get_position, set_position)
    velocity = property(get_velocity, set_velocity)
    timestamp = property(get_timestamp, set_timestamp)

    def move(self):
        new_position = self.position.add(self.velocity)
        self.set_position(new_position)
        return new_position.vector
