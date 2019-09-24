class Status:
    """This class represents three status meters: health, happiness, hunger."""
    min_meter = 0
    max_meter = 100

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

    def __str__(self):
        return f"---------------------------------\n" \
               f" Health   : {round(self.health, 1)}\n" \
               f" Happiness: {round(self.happiness, 1)}\n" \
               f" Hunger   : {round(self.hunger, 1)}\n" \
               f"---------------------------------"

    def decrease_hunger(self, meter):
        """Decrease hunger by given meter. But meter can't be smaller than the min value.
        Return the decreased meter.
        :return: a float"""
        prev = self.hunger
        self.hunger = max(Status.min_meter, self.hunger - meter)
        return prev - self.hunger

    def increase_happiness(self, meter):
        """Increase happiness meter by given meter. But meter can't be bigger than the max value.
        Return the increased meter.
        :return: a float"""
        prev = self.happiness
        self.happiness = min(Status.max_meter, self.happiness + meter)
        return self.happiness - prev

    def adjust_status(self, adjust_rate, time_diff):
        """
        Adjust three status meters of a tamagotchi based on adjustment rates,
        health: decrease over time at a set rate per second
        happiness: decrease over time at a set rate per second
        hunger: Increase over time at a set rate per second
        :param: a Status object, adjustment rate
        """
        self.health = max(Status.min_meter, self.health - time_diff * adjust_rate.health)
        self.happiness = max(Status.min_meter, self.happiness - time_diff * adjust_rate.happiness)
        self.hunger = min(Status.max_meter, self.hunger + time_diff * adjust_rate.hunger)

