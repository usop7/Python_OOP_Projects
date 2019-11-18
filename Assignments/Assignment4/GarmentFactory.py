"""
This module embodies classes that are require to proceed of orders to make
various garments of various brands.
"""

import abc
import enum

class BrandEnum(enum.Enum):
    LULULIME = "LuluLime"
    PINEAPPLE_REPUBLIC = "Pineapple Republic"
    NIKA = "Nika"


class ShirtMen(abc.ABC):
    """
    This defines the interface for Men's shirts product.
    """

    def __init__(self, style, size, colour, textile):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile


class ShirtMenLuluLime(ShirtMen):
    """
    ShirtMenLuluLime is a LuluLime Men's shirts that a garment factory makes.
    """

    def __init__(self, style, size, colour, textile, sport_type,
                 num_hidden_pockets):
        super().__init__(style, size, colour, textile)
        self.sport_type = sport_type
        self.num_hidden_pockets = num_hidden_pockets


class ShirtMenPineappleRepublic(ShirtMen):
    """
    ShirtMenPineappleRepublic is a Pineapple Republic Men's shirts that
    a garment factory makes.
    """

    def __init__(self, style, size, colour, textile, require_ironing,
                 num_buttons):
        super().__init__(style, size, colour, textile)
        self.require_ironing = require_ironing
        self.num_buttons = num_buttons


class ShirtMenNika(ShirtMen):
    """
    ShirtMenNika is a Nika Men's shirts that a garment factory makes.
    """

    def __init__(self, style, size, colour, textile, sport_type):
        super().__init__(style, size, colour, textile)
        self.sport_type = sport_type


class ShirtWomen(abc.ABC):
    """
    This defines the interface for Women's shirts product.
    """

    def __init__(self, style, size, colour, textile):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile


class SockPairUnisex(abc.ABC):
    """
    This defines the interface for Socks product.
    """

    def __init__(self, style, size, colour, textile):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile