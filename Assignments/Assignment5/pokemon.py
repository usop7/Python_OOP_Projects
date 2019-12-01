"""
This module embodies classes that represent a pokemon, an ability, and
a move.
"""


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
        stats = f"\n{'-'*60}\n".join(map(str, self.stats))
        types = ", ".join(self.types)
        abilities = f"\n{'-'*60}\n".join(map(str, self.abilities))
        moves = f"\n{'-'*60}\n".join(map(str, self.moves))
        return f"\nName: {self.name}\n" \
               f"\nId: {self.pokemon_id}\n" \
               f"\nHeight: {self.height}\n" \
               f"\nWeight: {self.weight}\n" \
               f"\nTypes: {types}\n" \
               f"\n{'-'*60}\nStats\n{'-'*60}\n{stats}\n" \
               f"\n{'-'*60}\nAbilities\n{'-'*60}\n{abilities}\n" \
               f"\n{'-'*60}\nMoves\n{'-'*60}\n{moves}"


class Ability:
    """
    This class represents an ability.
    """

    def __init__(self, name: str, url: str = None, ability_id: int = None,
                 generation: str = None, effect: str = None,
                 effect_short: str = None, pokemon: list = None):
        self.name = name
        self.url = url
        self.ability_id = ability_id
        self.generation = generation
        self.effect = effect
        self.effect_short = effect_short
        self.pokemon = pokemon

    def __str__(self):
        """
        When the url attribute is not None, return only name and url.
        It None, return all other attributes except for url.
        :return: string
        """
        # regular mode (not expanded)
        if self.url is not None:
            return f"\nName: {self.name}" \
                   f"\nURL: {self.url}"
        # expanded mode
        else:
            pokemon = ", ".join(self.pokemon)
            return f"\nName: {self.name}\n" \
                   f"\nID: {self.ability_id}\n" \
                   f"\nGeneration: {self.generation}\n" \
                   f"\nEffect: {self.effect}\n" \
                   f"\nEffect (Short): {self.effect_short}\n" \
                   f"\nPokemon: {pokemon}"


class Move:
    """
    This class represents a Move effect.
    """

    def __init__(self, name: str, level: int = None, url: str = None,
                 move_id: int = None, generation: str = None,
                 accuracy: int = None, pp: int = None, power: int = None,
                 move_type: str = None, damage_class: str = None,
                 effect_short: str = None):
        self.name = name
        self.level = level
        self.url = url
        self.move_id = move_id
        self.generation = generation
        self.accuracy = accuracy
        self.pp = pp
        self.power = power
        self.move_type = move_type
        self.damage_class = damage_class
        self.effect_short = effect_short

    def __str__(self):
        """
        When the url attribute is not None, return only name, level and url.
        It None, return all other attributes except for level and url.
        :return: string
        """
        # regular mode (not expanded)
        if self.url is not None:
            return f"\nName: {self.name}" \
                   f"\nLevel: {self.level}" \
                   f"\nURL: {self.url}"
        # expanded mode
        else:
            return f"\nName: {self.name}\n" \
                   f"\nID: {self.move_id}\n" \
                   f"\nGeneration: {self.generation}\n" \
                   f"\nAccuracy: {self.accuracy}\n" \
                   f"\nPP: {self.pp}\n"\
                   f"\nPower: {self.power}\n" \
                   f"\nType: {self.move_type}\n" \
                   f"\nDamage Class: {self.damage_class}\n" \
                   f"\nEffect (Short): {self.effect_short}\n"


class Stat:
    """
    This class represents stats of a pokemon.
    """

    def __init__(self, name: str, base_stat: int = None, url: str = None,
                 stat_id: int = None, is_battle_only: bool = None):
        self.name = name
        self.base_stat = base_stat
        self.url = url
        self.stat_id = stat_id
        self.is_battle_only = is_battle_only

    def __str__(self):
        """
        When the url attribute is not None, return name, base stat and url.
        It None, return all other attributes except for url and base stat.
        :return: string
        """
        # regular mode (not expanded)
        if self.url is not None:
            return f"Name: {self.name}\n" \
                   f"Base Stat: {self.base_stat}\n" \
                   f"URL: {self.url}\n"
        # expanded mode
        else:
            return f"Name: {self.name}\n" \
                   f"ID: {self.stat_id}\n" \
                   f"Is Battle Only: {self.is_battle_only}\n"
