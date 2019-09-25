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

    def __str__(self):
        return f"{self.name} ({self.calorie} calorie)"


class FoodController:
    """This class embodies a list of food and food related methods."""

    @staticmethod
    def is_fav_food(food_name, fav_food_list):
        """
        Return True if a food item belongs to a fav food list.
        :param food_name: a String
        :param fav_food_list: a list
        :return: boolean
        """
        result = False
        for fav_food in fav_food_list:
            if fav_food == food_name:
                result = True
        return result

    def __init__(self):
        """
        Initialize a food  controller.
        """
        self._food_list = [
            Food("Chocolate", 20),
            Food("Beer", 10),
            Food("Church's chicken", 30),
            Food("Steak", 30),
            Food("Shrimp", 20),
            Food("Carrot", 10),
            Food("Android 17", 30),
            Food("Android 18", 30)
        ]

    def give_food_option(self):
        """
        Prompt user with food list, and return the selected food.
        :return: Food object
        """
        question = "Here is the list of food\n" \
                   "----------------------------------\n"
        i = 1
        for food in self._food_list:
            question += f"{i}: {food}\n"
            i += 1
        question += "----------------------------------\n" \
                    "Please select: "

        # Create a list of valid answers
        valid_answers = []
        i = 0
        while i <= len(self._food_list):
            valid_answers.append(str(i))
            i += 1

        # Repeat until the user enters the valid options
        answer = 0
        while answer not in valid_answers:
            answer = input(question)
        answer = int(answer)

        return self._food_list[int(answer)-1]
