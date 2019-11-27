"""
This module embodies classes that represent a pokemon, an ability, and
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


class Ability:
    """
    This class represents an ability.
    """

    def __init__(self, name: str, ability_id: int, generation: str,
                 effect: str, effect_short: str, pokemon: list):
        self.name = name
        self.ability_id = ability_id
        self.generation = generation
        self.effect = effect
        self.effect_short = effect_short
        self.pokemon = pokemon


class Move:
    """
    This class represents a Move effect.
    """

    def __init__(self, name: str, move_id: int, generation: str,
                 accuracy: int, pp: int, power: int, move_type: str,
                 damage_class: str, effect_short: str):
        self.name = name
        self.move_id = move_id
        self.generation = generation
        self.accuracy = accuracy
        self.pp = pp
        self.power = power
        self.move_type = move_type
        self.damage_class = damage_class
        self.effect_short = effect_short


