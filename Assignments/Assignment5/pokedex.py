"""
This module embodies a driver class that will run the program.
"""

import argparse
import aiohttp
import asyncio
import enum
from input_handler import FileHandler


class Mode(enum.Enum):
    """
    List the various query modes that the pokedex can execute.
    """
    POKEMON = "pokemon"
    ABILITY = "ability"
    MOVE = "move"


class Request:
    """
    The request object represents a request to get a data from the API.
    The request object comes with certain accompanying configuration options:
     - mode: Mode enum
     - input: { 'filename.txt' | 'name or id' }, filename must end with
        .txt extension.
     - expanded: boolean
      - output: 'filename.txt' or 'print' by default
    """

    def __init__(self, mode: Mode, input: list, expanded: bool, output: str):
        self.mode = mode
        self.input = input
        self.expanded = expanded
        self.output = output

    def __str__(self):
        return f"{self.mode.value} {self.input} {self.expanded} {self.output}"


class Pokedex:
    """
    This class represents an app that takes input from the terminal and
    displays the output either in the console or prints it out to a file
    as specified by the input.
    """

    BASE_URL = "https://pokeapi.co/api/v2/{}/{}"
    mode_map = {}

    @staticmethod
    def setup_request_commandline() -> Request:
        """
        Implements the argparse module to accept arguments via the command
        line. This function specifies what these arguments are and parses it
        into an object of type Request. If something goes wrong with
        provided arguments then the function prints an error message and
        exits the application.
        :return: The object of type Request with all the arguments provided
        in it.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("mode", help="The mode specifies which information"
                                         "to query. This needs to be among"
                                         "pokemon, ability, or move.")
        parser.add_argument("input", help="The id or name that you want to"
                                          "search for. It must be a file name"
                                          "that ends with '.txt' extension"
                                          "or a string or an int.")
        parser.add_argument("--expanded", action="store_true",
                            help="With the expanded flag, pokedex will query "
                                 "more information. It only applies to"
                                 "to 'pokemon' mode.")
        parser.add_argument("--output", default="print",
                            help="The output of the program. This is 'print'"
                                 "by default, but can be set to a file name"
                                 "that ends with .txt extension.")
        try:
            args = parser.parse_args()
            input_data = FileHandler.load_input(args.input)
            request = Request(Mode(args.mode.lower()), input_data,
                              args.expanded, args.output)
            print(request)
            return request
        except Exception as e:
            print(f"Error! Could not read arguments.\n{e}")
            quit()

    @staticmethod
    async def get_pokemon_data(id: int, session: aiohttp.ClientSession):
        """
        An async function that retrieves an asynchronous API query of
        a pokemon with the given id/name.
        """
        target_url = Pokedex.BASE_URL.format("pokemon", id)
        response = await session.request(method="GET", url=target_url)
        json_dict = await response.json()
        print(json_dict)

    @staticmethod
    async def get_data(id: int):
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(Pokedex.get_pokemon_data(id, session))


def main():
    pokedex = Pokedex()
    request = pokedex.setup_request_commandline()
    #asyncio.run(pokedex.get_data(request.input))


if __name__ == '__main__':
    main()
