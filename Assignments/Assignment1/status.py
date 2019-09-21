class Status:
    """This class represents three status meters: health, happiness, hunger."""

    def __init__(self, health, happiness, hunger):
        """
        Initialize a status object with three meters.
        :param health: a float
        :param happiness: a float
        :param hunger: a float
        """
        self.health = health
        self.happiness = happiness
        self.hunger = hunger

    def get_status(self):
        """
        Return three status as a Tuple.
        :return: a Tuple(health, happiness, hunger)
        """
        status = (self.health, self.happiness, self.hunger)
        return status
