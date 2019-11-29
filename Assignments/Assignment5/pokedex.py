"""
This module embodies a driver class that will run the program.
"""

import aiohttp
import asyncio
from input_handler import IOHandler, Mode
from pokemon import Pokemon, PokemonStat, PokemonAbility, PokemonMove, \
     Ability, Move


class Pokedex:
    """
    This class represents an app that takes input from the terminal and
    displays the output either in the console or prints it out to a file
    as specified by the input.
    """

    BASE_URL = "https://pokeapi.co/api/v2/{}/{}"

    def __init__(self):
        """
        Create a Request object based on the user command, and assign it
        to a request attribute.
        """
        self.request = IOHandler.setup_request_commandline()
        self.pokemon_list = []
        self.ability_list = []
        self.move_list = []
        self.query_map = {
            Mode.POKEMON: self.create_pokemon,
            Mode.ABILITY: self.create_ability,
            Mode.MOVE: self.create_move
        }
        self.result_map = {
            Mode.POKEMON: self.pokemon_list,
            Mode.ABILITY: self.ability_list,
            Mode.MOVE: self.move_list
        }

    def process_request(self):
        """
        Process the request.
        """
        asyncio.run(self.process_async_tasks(
            self.request.mode,
            self.request.params,
            False
        ))

    async def process_task(self, mode: Mode, session: aiohttp.ClientSession,
                           param: str, is_param_url: bool):
        """
        An async function that retrieves an asynchronous API query of
        a pokemon/ability/move data with the given id/name.
        Then it creates a corresponding object based on its query mode.
        """
        target_url = Pokedex.BASE_URL.format(mode.value, param) \
            if not is_param_url else param
        try:
            response = await session.request(method="GET", url=target_url)
            json_dict = await response.json()
        except Exception as e:
            print(f"Error! Could not finish the query!\n{e}\n")
        else:
            obj = await self.query_map[mode](json_dict)
            self.result_map[mode].append(obj)

    async def process_async_tasks(self, mode: Mode, params: list,
                                  is_param_url: bool):
        """
        Create a list of multiple async tasks and run concurrently.
        """
        async with aiohttp.ClientSession() as session:
            tasks = [asyncio.create_task(self.process_task(mode, session,
                                                           p, is_param_url))
                     for p in params]
            await asyncio.gather(*tasks)

    def create_pokemon_stat_list(self, data: list) -> list:
        """
        Create a list of PokemonStat objects based on the given data.
        :param data: list of dictionaries
        :return: list of PokemonStat objects
        """
        stats = [
            PokemonStat(d["stat"]["name"],
                        d["base_stat"],
                        d["stat"]["url"] if self.request.expanded else None)
            for d in data]
        return stats

    async def create_pokemon_ability_list(self, data: list) -> list:
        """
        Create a list of PokemonAbility objects based on the given data.
        :param data: list of dictionaries
        :return: list of PokemonAbility objects
        """
        if not self.request.expanded:
            abilities = [
                Ability(name=d["ability"]["name"], url=d["ability"]["url"])
                for d in data]
            return abilities
        else:
            params = [d["ability"]["url"] for d in data]
            await self.process_async_tasks(Mode.ABILITY, params, True)
            return self.ability_list

    def create_pokemon_move_list(self, data: list) -> list:
        """
        Create a list of PokemonMove objects based on the given data.
        :param data: a dictionary
        :return: list of PokemonMove objects
        """
        moves = [
            PokemonMove(d["move"]["name"],
                        d["version_group_details"][0]["level_learned_at"],
                        d["move"]["url"] if self.request.expanded else None)
            for d in data]
        return moves

    async def create_pokemon(self, data: dict) -> Pokemon:
        """
        Create a Pokemon object based on the given data, and return it.
        :param data: list of dictionaries
        :return: Pokemon object
        """
        stat_list = self.create_pokemon_stat_list(data["stats"])
        ability_list = await self.create_pokemon_ability_list(data["abilities"])
        move_list = self.create_pokemon_move_list(data["moves"])
        type_list = [q["type"]["name"] for q in data["types"]]
        return Pokemon(data["name"], data["id"], data["height"],
                       data["weight"], stat_list, type_list,
                       ability_list, move_list)

    async def create_ability(self, data: dict) -> Ability:
        """
        Create an Ability object based on the given data, and return it.
        :param data: a dictionary
        :return: Pokemon object
        """
        pokemon = [q["pokemon"]["name"] for q in data["pokemon"]]
        return Ability(data["name"], ability_id=data["id"],
                       generation=data["generation"]["name"],
                       effect=data["effect_entries"][0]["effect"],
                       effect_short=data["effect_entries"][0]["short_effect"],
                       pokemon=pokemon)

    def create_move(self, data: dict) -> Move:
        """
        Create an Move object based on the given data, and return it.
        :param data: a dictionary
        :return: Pokemon object
        """
        return Move(data["name"], data["id"],
                    data["generation"]["name"],
                    data["accuracy"], data["pp"], data["power"],
                    data["type"]["name"],
                    data["damage_class"]["name"],
                    data["effect_entries"][0]["short_effect"])

    def print_report(self):
        """
        Print the query results of all input values.
        If there's more than one result, it will be separated by a dotted line.
        """
        # convert a list of objects to a string
        result_list = self.result_map[self.request.mode]
        result_str = f"\n\n{'-' * 60}\n\n".join(map(str, result_list))

        print(f"{'-'*20}Query Result{'-'*20}\n")
        if self.request.output == "print":
            print(result_str)
        else:
            IOHandler.write_data(self.request.output, result_str)
            print(f"Result written in '{self.request.output}'")


def main():
    pokedex = Pokedex()
    pokedex.process_request()
    pokedex.print_report()


if __name__ == '__main__':
    main()
