class Game:
    """This class represents a mini game."""

    def __init__(self, name, output, level_of_fun):
        """
        Initialize a mini game.
        :param name: a String
        :param output: a String
        :param level_of_fun: a float
        """
        self.name = name
        self.output = output
        self.level_of_fun = level_of_fun

    def __str__(self):
        return f"{self.name} (level of fun: {self.level_of_fun})"


class GameController:
    """This class embodies a list of mini games and game related methods."""

    def __init__(self):
        self._game_list = [
            Game("Fight with Goku", "What a great match!", 20),
            Game("Strongest under the heaven match", "Human beings were stronger than I thought.", 15),
            Game("Dragon balls search", "I ended up founding 3 dragon balls!", 10)
        ]

    def give_game_option(self):
        """
        Prompt user with game list, and return the selected game.
        :return: Game object
        """
        question = "Here is the list of games\n"
        i = 1
        for game in self._game_list:
            question += f"{i}: {game}\n"
            i += 1
        question += "Please select: "

        # Create a list of valid answers
        valid_answers = []
        i = 0
        while i <= len(self._game_list):
            valid_answers.append(str(i))
            i += 1

        # Repeat until the user enters the valid options
        answer = 0
        while answer not in valid_answers:
            answer = input(question)
        answer = int(answer)

        return self._game_list[int(answer)-1]
