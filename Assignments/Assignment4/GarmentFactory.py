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

    def __init__(self, style, size, colour, textile, in_or_out):
        super().__init__(style, size, colour, textile)
        self.in_or_out = in_or_out


class ShirtWomen(abc.ABC):
    """
    This defines the interface for Women's shirts product.
    """

    def __init__(self, style, size, colour, textile):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile


class ShirtWomenLuluLime(ShirtWomen):
    """
    ShirtWomenLuluLime is a LuluLime Women's shirts that a garment factory
    makes.
    """

    def __init__(self, style, size, colour, textile, sport_type,
                 num_hidden_pockets):
        super().__init__(style, size, colour, textile)
        self.sport_type = sport_type
        self.num_hidden_pockets = num_hidden_pockets


class ShirtWomenPineappleRepublic(ShirtWomen):
    """
    ShirtWomenPineappleRepublic is a Pineapple Republic Women's shirts that
    a garment factory makes.
    """

    def __init__(self, style, size, colour, textile, require_ironing,
                 num_buttons):
        super().__init__(style, size, colour, textile)
        self.require_ironing = require_ironing
        self.num_buttons = num_buttons


class ShirtWomenNika(ShirtWomen):
    """
    ShirtWomenNika is a Nika Women's shirts that a garment factory makes.
    """

    def __init__(self, style, size, colour, textile, in_or_out):
        super().__init__(style, size, colour, textile)
        self.in_or_out = in_or_out


class SockPairUnisex(abc.ABC):
    """
    This defines the interface for Socks product.
    """

    def __init__(self, style, size, colour, textile):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile


class SockPairUnisexLuluLime(SockPairUnisex):
    """
    SockPairUnisexLuluLime is a LuluLime's socks product that a garment factory
    makes.
    """

    def __init__(self, style, size, colour, textile, contain_silver,
                 stripe):
        super().__init__(style, size, colour, textile)
        self.contain_silver = contain_silver
        self.stripe = stripe


class SockPairUnisexPineappleRepublic(SockPairUnisex):
    """
    SockPairUnisexPineappleRepublic is a Pineapple Republic socks product that
    a garment factory makes.
    """

    def __init__(self, style, size, colour, textile, require_drycleaning):
        super().__init__(style, size, colour, textile)
        self.require_drycleaning = require_drycleaning


class SockPairUnisexNika(SockPairUnisex):
    """
    SockPairUnisexNika is a Nika socks product that a garment factory makes.
    """

    def __init__(self, style, size, colour, textile, articulated, length):
        super().__init__(style, size, colour, textile)
        self.articulated = articulated
        self.length = length


class Order:
    def __init__(self, date=None, number=None, brand=None, garment=None,
                 count=None, style=None, size=None, colour=None, textile=None,
                 sport_type=None, num_hidden_pockets=None,
                 require_drycleaning=None, in_or_out=None,
                 require_ironing=None, num_buttons=None, articulated=None,
                 length=None, contain_silver=None, stripe=None):
        self.date = date
        self.number = number
        self.brand = brand
        self.garment = garment
        self.count = count
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile
        self.sport_type = sport_type
        self.num_hidden_pockets = num_hidden_pockets
        self.require_drycleaning = require_drycleaning
        self.in_or_out = in_or_out
        self.require_ironing = require_ironing
        self.num_buttons = num_buttons
        self.articulated = articulated
        self.length = length
        self.contain_silver = contain_silver
        self.stripe = stripe


class BrandFactory(abc.ABC):
    """
    The base factory class. All brands expect this factory class to populate
    the brand. The BrandFactory class defines an interface to create a
    Product famiily consisting of Men's shirts, Women's shirts, and Socks.
    These vary by Brand.
    """

    @abc.abstractmethod
    def create_shirt_men(self, order: Order) -> ShirtMen:
        pass

    @abc.abstractmethod
    def create_shirt_women(self, order: Order) -> ShirtWomen:
        pass

    @abc.abstractmethod
    def create_socks_unisex(self, order: Order) -> SockPairUnisex:
        pass


class LululimeFactory(BrandFactory):
    """
    This factory class implements the BrandFactory Interface. It returns
    a product family consisting of ShirtMen, ShirtWomen, and SockPairUnisex
    for the brand LuluLime.
    """

    def create_shirt_men(self, order: Order) -> ShirtMen:
        return ShirtMenLuluLime(order.style, order.size, order.colour,
                                order.textile, order.sport_type,
                                order.num_hidden_pockets)

    def create_shirt_women(self, order: Order) -> ShirtWomen:
        return ShirtWomenLuluLime(order.style, order.size, order.colour,
                                  order.textile, order.sport_type,
                                order.num_hidden_pockets)

    def create_socks_unisex(self, order: Order) -> SockPairUnisex:
        return SockPairUnisexLuluLime(order.style, order.size, order.colour,
                                      order.textile, order.contain_silver,
                                      order.stripe)


class PineappleRepublicFactory(BrandFactory):
    """
    This factory class implements the BrandFactory Interface. It returns
    a product family consisting of ShirtMen, ShirtWomen, and SockPairUnisex
    for the brand Pineapple Republic.
    """

    def create_shirt_men(self, order: Order) -> ShirtMen:
        return ShirtMenPineappleRepublic(order.style, order.size, order.colour,
                                         order.textile, order.sport_type,
                                         order.num_hidden_pockets)

    def create_shirt_women(self, order: Order) -> ShirtWomen:
        return ShirtWomenPineappleRepublic(order.style, order.size,
                                           order.colour, order.textile,
                                           order.require_ironing,
                                           order.num_buttons)

    def create_socks_unisex(self, order: Order) -> SockPairUnisex:
        return SockPairUnisexPineappleRepublic(order.style, order.size,
                                               order.colour, order.textile,
                                               order.require_drycleaning)


class NikaFactory(BrandFactory):
    """
    This factory class implements the BrandFactory Interface. It returns
    a product family consisting of ShirtMen, ShirtWomen, and SockPairUnisex
    for the brand Nika.
    """

    def create_shirt_men(self, order: Order) -> ShirtMen:
        return ShirtMenNika(order.style, order.size, order.colour,
                            order.textile, order.in_or_out)

    def create_shirt_women(self, order: Order) -> ShirtWomen:
        return ShirtWomenNika(order.style, order.size, order.colour,
                              order.textile, order.in_or_out)

    def create_socks_unisex(self, order: Order) -> SockPairUnisex:
        return SockPairUnisexNika(order.style, order.size, order.colour,
                                  order.textile, order.articulated,
                                  order.length)



