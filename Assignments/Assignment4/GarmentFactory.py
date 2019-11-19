"""
This module embodies classes that are require to proceed of orders to make
various garments of various brands.
"""

import abc
import enum
import pandas as pd
import xlrd


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

    def __str__(self):
        return f"Style name: {self.style}, Size: {self.size}, " \
               f"Colour: {self.colour}, Textile: {self.textile}"


class ShirtMenLuluLime(ShirtMen):
    """
    ShirtMenLuluLime is a LuluLime Men's shirts that a garment factory makes.
    """

    def __init__(self, style, size, colour, textile, sport_type,
                 num_hidden_pockets):
        super().__init__(style, size, colour, textile)
        self.sport_type = sport_type
        self.num_hidden_pockets = num_hidden_pockets

    def __str__(self):
        return f"{self.__class__.__name__}:: " \
               f"{super().__str__()}, Sport: {self.sport_type}," \
               f"Hidden Zipper Pockets: {self.num_hidden_pockets}"


class ShirtMenPineappleRepublic(ShirtMen):
    """
    ShirtMenPineappleRepublic is a Pineapple Republic Men's shirts that
    a garment factory makes.
    """

    def __init__(self, style, size, colour, textile, req_ironing,
                 num_buttons):
        super().__init__(style, size, colour, textile)
        self.req_ironing = req_ironing
        self.num_buttons = num_buttons

    def __str__(self):
        return f"{self.__class__.__name__}:: " \
               f"{super().__str__()}, Dry Cleaning: {self.req_ironing}," \
               f"Buttons: {self.num_buttons}"


class ShirtMenNika(ShirtMen):
    """
    ShirtMenNika is a Nika Men's shirts that a garment factory makes.
    """

    def __init__(self, style, size, colour, textile, in_or_out):
        super().__init__(style, size, colour, textile)
        self.in_or_out = in_or_out

    def __str__(self):
        return f"{self.__class__.__name__}:: " \
               f"{super().__str__()}, Indoor/Outdoor: {self.in_or_out}"


class ShirtWomen(abc.ABC):
    """
    This defines the interface for Women's shirts product.
    """

    def __init__(self, style, size, colour, textile):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile

    def __str__(self):
        return f"Style name: {self.style}, Size: {self.size}, " \
               f"Colour: {self.colour}, Textile: {self.textile}"


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

    def __str__(self):
        return f"{self.__class__.__name__}:: " \
               f"{super().__str__()}, Sport: {self.sport_type}," \
               f"Hidden Zipper Pockets: {self.num_hidden_pockets}"


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

    def __str__(self):
        return f"{self.__class__.__name__}:: " \
               f"{super().__str__()}, Indoor/Outdoor: {self.in_or_out}"


class SockPairUnisex(abc.ABC):
    """
    This defines the interface for Socks product.
    """

    def __init__(self, style, size, colour, textile):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile

    def __str__(self):
        return f"Style name: {self.style}, Size: {self.size}, " \
               f"Colour: {self.colour}, Textile: {self.textile}"


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

    def __str__(self):
        return f"{self.__class__.__name__}:: " \
               f"{super().__str__()}, Silver: {self.contain_silver}, " \
               f"Stripe: {self.stripe}"


class SockPairUnisexPineappleRepublic(SockPairUnisex):
    """
    SockPairUnisexPineappleRepublic is a Pineapple Republic socks product that
    a garment factory makes.
    """

    def __init__(self, style, size, colour, textile, dry_cleaning):
        super().__init__(style, size, colour, textile)
        self.dry_cleaning = dry_cleaning

    def __str__(self):
        return f"{self.__class__.__name__}:: " \
               f"{super().__str__()}, Dry Cleaning: {self.dry_cleaning}"


class SockPairUnisexNika(SockPairUnisex):
    """
    SockPairUnisexNika is a Nika socks product that a garment factory makes.
    """

    def __init__(self, style, size, colour, textile, articulated, length):
        super().__init__(style, size, colour, textile)
        self.articulated = articulated
        self.length = length
        
    def __str__(self):
        return f"{self.__class__.__name__}:: " \
               f"{super().__str__()}, Articulated: {self.articulated}, " \
               f"Length: {self.length}"


class Order:
    def __init__(self, number=None, date=None, brand=None, garment=None,
                 count=None, style=None, size=None, colour=None, textile=None,
                 sport_type=None, num_hidden_pockets=None,
                 require_drycleaning=None, in_or_out=None,
                 require_ironing=None, num_buttons=None, articulated=None,
                 length=None, contain_silver=None, stripe=None):
        self.number = number
        self.date = date
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


class OrderProcessor:
    """
    Maintains a mapping of brand -> BrandFactory. The OrderProcessor
    is responsible for retrieving the right factory for the specified brand.
    """

    # Map Brand types to their respective factories
    brand_map = {
        "Lululime": LululimeFactory,
        "PineappleRepublic": PineappleRepublicFactory,
        "Nika": NikaFactory
    }
    order_list = {}

    @staticmethod
    def get_product_type(order):
        """
        Return the product type.
        :param order: an Order object
        :return: String
        """
        return order.garment

    def get_factory(self, order: Order) -> BrandFactory:
        """
        Retrieves the associated factory for the specified BrandEnum
        """
        brand_type = order.brand
        factory_class = self.brand_map.get(brand_type, None)
        return factory_class()

    def open_order_sheet(self):
        """
        Aks users the name of the excel spreadsheet and read the spreadsheet.
        Iterate each row and process the order.
        """
        #file_path = input("Please enter the excel file name: ")
        file_path = "COMP_3522_A4_orders.xlsx"
        df = pd.read_excel(file_path)
        for _, row in df.iterrows():
            self.process_next_order(row)

    def process_next_order(self, row):
        """
        Convert each row to an Order object and store it
        in the order_list dictionary as {Order Number: Order object}
        :param row: data frame row
        """
        order = Order(row['Order Number'], row['Date'], row['Brand'],
                      row['Garment'], row['Count'], row['Style name'],
                      row['Size'], row['Colour'], row['Textile'], row['Sport'],
                      row['Hidden Zipper Pockets'], row['Dry Cleaning'],
                      row['Indoor/Outdoor'], row['Requires Ironing'],
                      row['Buttons'], row['Articulated'], row['Length'],
                      row['Silver'], row['Stripe'])
        self.order_list[row['Order Number']] = order


class GarmentMaker:
    """
    Defines a Garment Factory that makes of Men's shirts, Women's shirts
    and Socks. Each product has a brand.
    """

    def __init__(self):
        self.order_processor = OrderProcessor()
        self.shirts_men = []
        self.shirts_women = []
        self.socks_unisex = []
        self.product_map = {
            "ShirtMen": self.shirts_men,
            "ShirtWomen": self.shirts_women,
            "SockPairUnisex": self.socks_unisex
        }

    def shirt_men_maker(self, order):
        """
        Make men's shirts with the specified brand factory.
        :param order: an Order
        """
        factory = self.order_processor.get_factory(order)
        factory.create_shirt_men(order)

    def shirt_women_maker(self, order):
        """
        Make women's shirts with the specified brand factory.
        :param order: an Order
        """
        factory = self.order_processor.get_factory(order)
        factory.create_shirt_women(order)

    def socks_unisex_maker(self, order):
        """
        Make unisex socks with the specified brand factory.
        :param order: an Order
        """
        factory = self.order_processor.get_factory(order)
        factory.create_socks_unisex(order)

    def place_orders(self):
        """
        Iterate each order in the order list, and add it
        to a corresponding list.
        """
        for order in self.order_processor.order_list:
            product = self.order_processor.get_product_type(order)
            self.product_map.get(product).append(order)

    def send_orders(self):
        for order in self.shirts_men:
            self.shirt_men_maker(order)

        for order in self.shirts_women:
            self.shirt_men_maker(order)

        for order in self.socks_unisex:
            self.socks_unisex_maker(order)







def main():
    garment_maker = GarmentMaker()
    garment_maker.order_processor.open_order_sheet()


if __name__ == '__main__':
    main()


