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

    def __str__(self):
        url = ""
        if self.url is not None:
            url = f"\tURL: {self.url}\n"
        return f"\tName: {self.name}\n" \
               f"\tBase Stat: {self.base_stat}\n{url}"


class PokemonAbility:
    """
    This class represents an ability of a pokemon.
    """

    def __init__(self, name: str, url: str = None):
        self.name = name
        self.url = url

    def __str__(self):
        url = ""
        if self.url is not None:
            url = f"\tURL: {self.url}\n"
        return f"\tName: {self.name}\n{url}"


class PokemonMove:
    """
    This class represents a move of a pokemon.
    """

    def __init__(self, name: str, level: int, url: str = None):
        self.name = name
        self.level = level
        self.url = url

    def __str__(self):
        url = ""
        if self.url is not None:
            url = f"\tURL: {self.url}\n"
        return f"\tName: {self.name}\n" \
               f"\tLevel: {self.level}\n{url}"


class Pokemon:
    """
    This class represents a pokemon.
    """

    def __init__(self, name: str, pokemon_id: int, height: int, weight: int,
                 stats: list, types: list, abilities: list, moves: list):
        self.name = name
        self.pokemon_id = pokemon_id
        self.height = height
        self.weight = weight
        self.stats = stats
        self.types = types
        self.abilities = abilities
        self.moves = moves

    def __str__(self):
        stats = "\n".join(map(str, self.stats))
        types = ", ".join(self.types)
        abilities = "\n".join(map(str, self.abilities))
        moves = "\n".join(map(str, self.moves))
        return f"\nName: {self.name}\n" \
               f"\nId: {self.pokemon_id}\n" \
               f"\nHeight: {self.height}\n" \
               f"\nWeight: {self.weight}\n" \
               f"\nTypes: {types}\n" \
               f"\nStats:\n{stats}\n" \
               f"\nAbilities:\n{abilities}\n" \
               f"\nMoves:\n{moves}"


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

    def __str__(self):
        pokemon = ", ".join(self.pokemon)
        return f"\nName: {self.name}\n" \
               f"\nID: {self.ability_id}\n" \
               f"\nGeneration: {self.generation}\n" \
               f"\nEffect:\n{self.effect}\n" \
               f"\nEffect (Short): {self.effect_short}\n" \
               f"\nPokemon:\n{pokemon}"


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

    def __str__(self):
        return f"\nName: {self.name}\n" \
               f"\nID: {self.move_id}\n" \
               f"\nGeneration: {self.generation}\n" \
               f"\nAccuracy: {self.accuracy}\n" \
               f"\nPP: {self.pp}\n"\
               f"\nPower: {self.power}\n" \
               f"\nType: {self.move_type}\n" \
               f"\nDamage Class: {self.damage_class}\n" \
               f"\nEffect (Short): {self.effect_short}\n"


