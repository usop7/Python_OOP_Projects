"""
This module embodies a driver class(Pokedex) that runs the program.
"""

import aiohttp
import asyncio

from input_handler import IOHandler, Mode
from pokemon import Pokemon, Ability, Move, Stat


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
        query_map: maps Mode enum to a corresponding API query method.
        result_map: maps Mode enum to a corresponding list to hold results.
        """
        self.request = IOHandler.setup_request_commandline()
        self.pokemon_list = []
        self.ability_list = []
        self.move_list = []
        self.stat_list = []
        self.error_msg = []
        self.query_map = {
            Mode.POKEMON: self.create_pokemon,
            Mode.ABILITY: self.create_ability,
            Mode.MOVE: self.create_move,
            Mode.STAT: self.create_stat
        }
        self.result_map = {
            Mode.POKEMON: self.pokemon_list,
            Mode.ABILITY: self.ability_list,
            Mode.MOVE: self.move_list,
            Mode.STAT: self.stat_list
        }

    def process_request(self):
        """
        Process the request.
        Pass request mode and its parameters to the async method.
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

        :is_param_url: param can be passed as 'name or id' or
        as a  'full url'. If true, that means it's a full url.
        """
        target_url = Pokedex.BASE_URL.format(mode.value, param) \
            if not is_param_url else param
        try:
            response = await session.request(method="GET", url=target_url)
            json_dict = await response.json()
        except aiohttp.ContentTypeError:
            self.error_msg.append(f"Input Error! Could not find the input "
                                  f"value '{param}'\n")
        except aiohttp.ClientConnectorError:
            self.error_msg.append(f"Connection Error! Please check your "
                                  f"network status. Could not finish the"
                                  f"query for the input '{param}'\n")
        except Exception:
            self.error_msg.append(f"Unknown Error! Could not finish the query "
                                  f"for the input '{param}'\n")
        else:
            obj = await self.query_map[mode](json_dict)
            self.result_map[mode].append(obj)

    async def process_async_tasks(self, mode: Mode, params: list,
                                  is_param_url: bool):
        """
        Create a list of multiple async tasks and run concurrently.
        :is_param_url: param can be passed as 'name or id' or
        as a  'full url'. If true, that means it's a full url type.
        """
        async with aiohttp.ClientSession() as session:
            tasks = [asyncio.create_task(self.process_task(mode, session,
                                                           p, is_param_url))
                     for p in params]
            await asyncio.gather(*tasks)

    async def create_pokemon_stat_list(self, data: list) -> list:
        """
        If not an expanded mode, create a list of Stat objects based on
        the given data, and return the list.
        If an expanded mode, pass a list of url parameters to the
        async tasks method, and then return the stat_list.
        :param data: list of dictionaries
        :return: list of Stat objects
        """
        if not self.request.expanded:
            stats = [
                Stat(name=d["stat"]["name"], base_stat=d["base_stat"],
                     url=d["stat"]["url"])
                for d in data]
            return stats
        else:
            params = [d["stat"]["url"] for d in data]
            await self.process_async_tasks(Mode.STAT, params, True)
            return self.stat_list

    async def create_pokemon_ability_list(self, data: list) -> list:
        """
        If not an expanded mode, create a list of Ability objects based on
        the given data, and return the list.
        If an expanded mode, pass a list of url parameters to the
        async tasks method, and then return the ability_list.
        :param data: list of dictionaries
        :return: list of Ability objects
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

    async def create_pokemon_move_list(self, data: list) -> list:
        """
        If not an expanded mode, create a list of Move objects based on
        the given data, and return the list.
        If an expanded mode, pass a list of url parameters to the
        async tasks method, and then return the move_list.
        :param data: list of dictionaries
        :return: list of Move objects
        """
        if not self.request.expanded:
            moves = [
                Move(name=d["move"]["name"],
                     level=d["version_group_details"][0]["level_learned_at"],
                     url=d["move"]["url"])
                for d in data]
            return moves
        else:
            params = [d["move"]["url"] for d in data]
            await self.process_async_tasks(Mode.MOVE, params, True)
            return self.move_list

    async def create_pokemon(self, data: dict) -> Pokemon:
        """
        Create a Pokemon object based on the given data, and return it.
        :param data: list of dictionaries
        :return: Pokemon object
        """
        stats = await self.create_pokemon_stat_list(data["stats"])
        abilities = await self.create_pokemon_ability_list(data["abilities"])
        moves = await self.create_pokemon_move_list(data["moves"])
        types = [q["type"]["name"] for q in data["types"]]
        return Pokemon(data["name"], data["id"], data["height"],
                       data["weight"], stats, types,
                       abilities, moves)

    async def create_ability(self, data: dict) -> Ability:
        """
        Create an Ability object based on the given data, and return it.
        :param data: a dictionary
        :return: Pokemon object
        """
        pokemon = [q["pokemon"]["name"] for q in data["pokemon"]]
        return Ability(name=data["name"], ability_id=data["id"],
                       generation=data["generation"]["name"],
                       effect=data["effect_entries"][0]["effect"],
                       effect_short=data["effect_entries"][0]["short_effect"],
                       pokemon=pokemon)

    async def create_move(self, data: dict) -> Move:
        """
        Create an Move object based on the given data, and return it.
        :param data: a dictionary
        :return: Pokemon object
        """
        return Move(name=data["name"], move_id=data["id"],
                    generation=data["generation"]["name"],
                    accuracy=data["accuracy"], pp=data["pp"],
                    power=data["power"], move_type=data["type"]["name"],
                    damage_class=data["damage_class"]["name"],
                    effect_short=data["effect_entries"][0]["short_effect"])

    async def create_stat(self, data: dict) -> Move:
        """
        Create an Stat object based on the given data, and return it.
        :param data: a dictionary
        :return: Stat object
        """
        return Stat(name=data["name"], stat_id=data["id"],
                    is_battle_only=data["is_battle_only"])

    def print_report(self):
        """
        Print the query results of all input values.
        Depending on the request's output mode, it will be printed to the
        console or a specified output file.
        It there's an error occurred, it will be printed on the top of results.
        If there's more than one result, it will be separated by a '==' line.
        """
        # convert a list of error messages to a string (if any)
        errors = f"\n".join(self.error_msg)

        # convert a list of objects to a string
        result_list = self.result_map[self.request.mode]
        results = f"\n\n\n{'=' * 80}\n\n\n".join(map(str, result_list))

        # print the results (to the console or a file)
        print(f"{'='*30} Query Result {'='*30}\n")
        if self.request.output == "print":
            print(errors)
            print(results)
        else:
            IOHandler.write_data(self.request.output, errors + results)
            print(f"Result written in '{self.request.output}'")


def main():
    """
    Create a Pokedex object and process the request.
    Then, print the query results.
    """
    pokedex = Pokedex()
    pokedex.process_request()
    pokedex.print_report()


if __name__ == '__main__':
    main()
