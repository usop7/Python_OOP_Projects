"""
This module embodies classes that are require to proceed of orders to make
various garments of various brands.
"""

import abc
import enum
import pandas as pd
from input_handler import InputHandler


class BrandEnum(enum.Enum):
    LULULIME = "Lululime"
    PINEAPPLE_REPUBLIC = "PineappleRepublic"
    NIKA = "Nika"


class GarmentEnum(enum.Enum):
    SHIRT_MEN = "ShirtMen"
    SHIRT_WOMEN = "ShirtWomen"
    SOCK_UNISEX = "SockPairUnisex"


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
               f"{super().__str__()}, Sport: {self.sport_type}, " \
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
               f"{super().__str__()}, Dry Cleaning: {self.req_ironing}, " \
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
               f"{super().__str__()}, Sport: {self.sport_type}, " \
               f"Hidden Zipper Pockets: {self.num_hidden_pockets}"


class ShirtWomenPineappleRepublic(ShirtWomen):
    """
    ShirtWomenPineappleRepublic is a Pineapple Republic Women's shirts that
    a garment factory makes.
    """

    def __init__(self, style, size, colour, textile, req_ironing,
                 num_buttons):
        super().__init__(style, size, colour, textile)
        self.req_ironing = req_ironing
        self.num_buttons = num_buttons

    def __str__(self):
        return f"{self.__class__.__name__}:: " \
               f"{super().__str__()}, Requires Ironing: {self.req_ironing}, " \
               f"Buttons: {self.num_buttons}"


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
    """
    This class represents an order of a garment with the details.
    """

    def __init__(self, order_number=None, date=None, brand=None, garment=None,
                 count=None, style=None, size=None, colour=None, textile=None,
                 sport=None, num_hidden_pockets=None,
                 dry_cleaning=None, in_or_out=None,
                 require_ironing=None, buttons=None, articulated=None,
                 length=None, silver=None, stripe=None):
        self.number = order_number
        self.date = date
        self.brand = BrandEnum(brand)
        self.garment = GarmentEnum(garment)
        self.count = int(count)
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile
        self.sport_type = sport
        self.num_hidden_pockets = int(num_hidden_pockets)
        self.dry_cleaning = dry_cleaning
        self.in_or_out = in_or_out
        self.require_ironing = require_ironing
        self.num_buttons = int(buttons)
        self.articulated = articulated
        self.length = length
        self.contain_silver = silver
        self.stripe = stripe

    def __str__(self):
        return f"{self.number}, {self.brand}, {self.garment}"


class BrandFactory(abc.ABC):
    """
    The base factory class. All brands expect this factory class to populate
    the brand. The BrandFactory class defines an interface to create a
    Product family consisting of Men's shirts, Women's shirts, and Socks.
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

    def create_shirt_men(self, order: Order) -> ShirtMenLuluLime:
        return ShirtMenLuluLime(order.style, order.size, order.colour,
                                order.textile, order.sport_type,
                                order.num_hidden_pockets)

    def create_shirt_women(self, order: Order) -> ShirtWomenLuluLime:
        return ShirtWomenLuluLime(order.style, order.size, order.colour,
                                  order.textile, order.sport_type,
                                  order.num_hidden_pockets)

    def create_socks_unisex(self, order: Order) -> SockPairUnisexLuluLime:
        return SockPairUnisexLuluLime(order.style, order.size, order.colour,
                                      order.textile, order.contain_silver,
                                      order.stripe)


class PineappleRepublicFactory(BrandFactory):
    """
    This factory class implements the BrandFactory Interface. It returns
    a product family consisting of ShirtMen, ShirtWomen, and SockPairUnisex
    for the brand Pineapple Republic.
    """

    def create_shirt_men(self, order: Order) -> ShirtMenPineappleRepublic:
        return ShirtMenPineappleRepublic(order.style, order.size, order.colour,
                                         order.textile, order.sport_type,
                                         order.num_hidden_pockets)

    def create_shirt_women(self, order: Order) -> ShirtWomenPineappleRepublic:
        return ShirtWomenPineappleRepublic(order.style, order.size,
                                           order.colour, order.textile,
                                           order.require_ironing,
                                           order.num_buttons)

    def create_socks_unisex(self, order: Order) \
            -> SockPairUnisexPineappleRepublic:
        return SockPairUnisexPineappleRepublic(order.style, order.size,
                                               order.colour, order.textile,
                                               order.dry_cleaning)


class NikaFactory(BrandFactory):
    """
    This factory class implements the BrandFactory Interface. It returns
    a product family consisting of ShirtMen, ShirtWomen, and SockPairUnisex
    for the brand Nika.
    """

    def create_shirt_men(self, order: Order) -> ShirtMenNika:
        return ShirtMenNika(order.style, order.size, order.colour,
                            order.textile, order.in_or_out)

    def create_shirt_women(self, order: Order) -> ShirtWomenNika:
        return ShirtWomenNika(order.style, order.size, order.colour,
                              order.textile, order.in_or_out)

    def create_socks_unisex(self, order: Order) -> SockPairUnisexNika:
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
        BrandEnum.LULULIME: LululimeFactory,
        BrandEnum.PINEAPPLE_REPUBLIC: PineappleRepublicFactory,
        BrandEnum.NIKA: NikaFactory
    }
    # Hold all the orders as a dictionary {order number: Order object}
    order_list = {}

    @staticmethod
    def get_order_number(order):
        """
        :param order: Order object
        :return: int
        """
        return order.number

    def get_factory(self, order: Order) -> BrandFactory:
        """
        Retrieves the associated factory for the specified BrandEnum
        """
        return self.brand_map.get(order.brand, None)()

    def open_order_sheet(self):
        """
        Aks users the name of the excel spreadsheet and read the spreadsheet.
        Iterate each row and process the order.
        """
        file_path = input("Please enter the excel file name: ")
        InputHandler.validate_file(file_path)
        df = pd.read_excel(file_path).fillna(0)
        df.columns = [column.lower() for column in df.columns]
        df.rename(columns={'order number': 'order_number',
                           'style name': 'style',
                           'hidden zipper pockets': 'num_hidden_pockets',
                           'dry cleaning': 'dry_cleaning',
                           'indoor/outdoor': 'in_or_out',
                           'requires ironing': 'require_ironing'},
                  inplace=True)
        for _, row in df.iterrows():
            self.process_next_order(row)

    def process_next_order(self, row):
        """
        Validate data and convert each row to an Order object and store it
        in the order_list dictionary as {Order Number: Order object}
        :param row: data frame row
        """
        # Validate Integer types
        InputHandler.validate_int(row['order_number'])
        InputHandler.validate_int(row['count'])
        InputHandler.validate_int(row['num_hidden_pockets'])
        InputHandler.validate_int(row['buttons'])
        self.order_list[row['order_number']] = Order(**row.to_dict())

    def get_garment(self, order_number):
        """
        Return a Garment of the given order number.
        :param order_number: an int
        :return: GarmentEnum
        """
        return self.order_list[order_number].garment

    def get_order_count(self, order_number):
        """
        Return a count of the given order number.
        :param order_number: an int
        :return: int
        """
        return self.order_list[order_number].count

    def get_brand(self, order_number):
        """
        Return a brand of the given order number.
        :param order_number: an int
        :return: String
        """
        return self.order_list[order_number].brand.value


class GarmentMaker:
    """
    Defines a Garment Factory that makes of Men's shirts, Women's shirts
    and Socks. Each product has a brand.
    """

    def __init__(self):
        self.order_processor = OrderProcessor()
        self.garment_map = {
            GarmentEnum.SHIRT_MEN: self.shirt_men_maker,
            GarmentEnum.SHIRT_WOMEN: self.shirt_women_maker,
            GarmentEnum.SOCK_UNISEX: self.socks_unisex_maker
        }
        self.garment_list = {}

    def shirt_men_maker(self, order):
        """
        Make men's shirts with the specified brand factory.
        :param order: an Order
        """
        factory = self.order_processor.get_factory(order)
        order_number = self.order_processor.get_order_number(order)
        count = self.order_processor.get_order_count(order_number)
        garment_list = [factory.create_shirt_men(order)
                        for _ in range(int(count))]
        self.garment_list[order_number] = garment_list

    def shirt_women_maker(self, order):
        """
        Make women's shirts with the specified brand factory.
        :param order: an Order
        """
        factory = self.order_processor.get_factory(order)
        order_number = self.order_processor.get_order_number(order)
        count = self.order_processor.get_order_count(order_number)
        garment_list = [factory.create_shirt_women(order)
                        for _ in range(int(count))]
        self.garment_list[order_number] = garment_list

    def socks_unisex_maker(self, order):
        """
        Make unisex socks with the specified brand factory.
        :param order: an Order
        """
        factory = self.order_processor.get_factory(order)
        order_number = self.order_processor.get_order_number(order)
        count = self.order_processor.get_order_count(order_number)
        garment_list = [factory.create_socks_unisex(order)
                        for _ in range(int(count))]
        self.garment_list[order_number] = garment_list

    def send_orders(self):
        """
        Iterate each order in the order list, and send it to a garment maker
        by mapping each garment type to a corresponding garment maker.
        """
        for num, order in self.order_processor.order_list.items():
            product = self.order_processor.get_garment(num)
            self.garment_map.get(product)(order)

    def generate_report(self):
        """
        Prints a report summarizing the day's work. The report contains
        a single line per order that includes a brand, a garment type,
        and a list of garments.
        """
        for num, products in sorted(self.garment_list.items()):
            print(f"\nOrder {num}: {self.order_processor.get_brand(num)} "
                  f"{self.order_processor.get_garment(num).value}")
            print(*products, sep=' ')


def main():
    """
    Instantiate a GarmentMaker, process each order in the order sheet,
    and prints out the report.
    """

    garment_maker = GarmentMaker()
    try:
        garment_maker.order_processor.open_order_sheet()
    except FileNotFoundError as e:
        print(f"{e}")
    except ValueError as e:
        print(f"{e}")
    except Exception as e:
        print(f"Unknown exception occurred!\n{e}")
    else:
        garment_maker.send_orders()
        garment_maker.generate_report()


if __name__ == '__main__':
    main()


