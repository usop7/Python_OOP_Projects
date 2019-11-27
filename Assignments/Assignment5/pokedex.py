"""
This module embodies a driver class that will run the program.
"""

import argparse
import aiohttp
import asyncio


class Request:
    """
    The request object represents a request to get a data from the API.
    The request object comes with certain accompanying configuration options:
     - mode: {'pokemon' | 'ability' | 'move}
     - input: { 'filename.txt' | 'name or id' }, filename must end with
        .txt extension.
    """

    def __init__(self, mode, input):
        self.mode = mode
        self.input = input

    def __str__(self):
        return f"{self.mode} {self.input}"


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
        parser.add_argument("mode", help="The mode should be among"
                                         "Pokemon, Ability, or Move.")
        parser.add_argument("input", help="The input that you want to"
                                          "search for. It must be a file name"
                                          "that ends with '.txt' extension"
                                          "or a name/id.")
        try:
            args = parser.parse_args()
            request = Request(args.mode, args.input)
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
    asyncio.run(pokedex.get_data(request.input))


if __name__ == '__main__':
    main()
