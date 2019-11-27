"""
This module emobides classes that represent a pokemon, an ability, and
a move.
"""


class PokemonStat:
    """
    This class represents stats of a pokemon.
    """

    def __init__(self, name: str, base_stat: int, url: str = None):
        self.name = name
        self.base_stat = base_stat
        self.url = url


class PokemonAbility:
    """
    This class represents an ability of a pokemon.
    """

    def __init__(self, name: str, url: str = None):
        self.name = name
        self.url = url


class PokemonMove:
    """
    This class represents a move of a pokemon.
    """

    def __init__(self, name: str, level: int, url: str = None):
        self.name = name
        self.level = level
        self.url = url


class Pokemon:
    """
    This class represents a pokemon.
    """

    def __init__(self, name: str, pokemon_id: int, height: int, weight: int,
                 stats: PokemonStat, types: PokemonAbility,
                 abilities: PokemonAbility, moves: PokemonMove):
        self.name = name
        self.pokemon_id = pokemon_id
        self.height = height
        self.weight = weight
        self.stats = stats
        self.types = types
        self.abilities = abilities
        self.moves = moves

