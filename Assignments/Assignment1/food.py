class Food:
    """This class represents a food item."""

    def __init__(self, name, calorie):
        """
        Initialize a food item.
        :param name: a String
        :param calorie: a float
        """
        self.name = name
        self.calorie = calorie


class FoodController:
    """This class embodies a list of food and food related methods."""

    @classmethod
    def _generate_food_items(cls):
        """
        Return a list of food items with dummy data
        :return: a list
        """
        food_list = [
            Food("Chocolate", 5),
            Food("Beer", 2),
            Food("Church's chicken", 10),
            Food("Steak", 5),
            Food("Shrimp", 1),
            Food("Human", 10),
            Food("Carrot", 3)
        ]
        return food_list

    def __init__(self, food_list):
        """
        Initialize a food  controller.
        """
        self._food_list = food_list

    def give_food_option(self):
        question = "Here is the list of food\n"
        i = 1
        for food in self._food_list:
            question += f"{i}: {food.name} ({food.calorie} calorie)\n"
            i += 1
        question += "Please select: "
        answer = int(input(question))
        return self._food_list[int(answer)-1]

