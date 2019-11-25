from unittest import TestCase
from garment_factory import GarmentMaker
from garment_factory import OrderProcessor
from garment_factory import Order
from garment_factory import LululimeFactory
from garment_factory import ShirtMenLuluLime
from garment_factory import ShirtWomenPineappleRepublic
from garment_factory import ShirtMen
from garment_factory import ShirtWomen
from garment_factory import SockPairUnisex
from garment_factory import SockPairUnisexNika


class TestOrderProcessor(TestCase):

    @staticmethod
    def create_lululime_shirtmen_order():
        """
        Creates a Order whose brand is Lululime and whose garment
        is Men's shirts.
        :return: Order
        """
        return Order(order_number="1", date="Friday November 16 2019",
                     brand="Lululime", garment="ShirtMen", count="3",
                     style="Bowen", size="M", colour="Grey",
                     textile="Merino wool",
                     sport="Yoga", num_hidden_pockets="1")

    @staticmethod
    def create_pineapple_shirtwomen_order():
        """
        Creates a Order whose brand is PineappleRepublic and whose garment
        is Women's shirts.
        :return: Order
        """
        return Order(order_number="1", date="Friday November 16 2019",
                     brand="PineappleRepublic", garment="ShirtWomen",
                     count="3", style="Bowen", size="M", colour="Grey",
                     textile="Merino wool", require_ironing="Y", buttons="6")

    @staticmethod
    def create_nika_socks_order():
        """
        Creates a Order whose brand is Nika and whose garment is socks.
        :return: Order
        """
        return Order(order_number="1", date="Friday November 16 2019",
                     brand="Nika", garment="ShirtWomen",
                     count="3", style="Bowen", size="M", colour="Grey",
                     textile="Merino wool", articulated="Y", length="Knee")

    @staticmethod
    def create_garment_maker():
        """
        Creates a dictionary object, and loads the file into it.
        :return: Dictionary
        """
        garment_maker = GarmentMaker()
        order = TestOrderProcessor.create_lululime_shirtmen_order()
        garment_maker.order_processor.order_list[0] = order
        return garment_maker

    def test_get_factory(self):
        """
        Unit test for get_factory. Asserts that the method returns
        LululimeFacotry when the order's brandtype is Lululime.
        """
        order_processor = OrderProcessor()
        order = TestOrderProcessor.create_lululime_shirtmen_order()
        factory = order_processor.get_factory(order)
        self.assertTrue(isinstance(factory, LululimeFactory))

    def test_create_shirt_men(self):
        """
        Unit test for create_shirt_men. Asserts that the method creates
        ShirtMen based on its order.
        """
        order_processor = OrderProcessor()
        order = TestOrderProcessor.create_lululime_shirtmen_order()
        factory = order_processor.get_factory(order)
        garment = factory.create_shirt_men(order)
        self.assertTrue(isinstance(garment, ShirtMen))

    def test_shirt_men_maker(self):
        """
        Unit test for shirt_men_maker. Asserts that the method creates
        ShirtMenLuluLime and stores it in the garment_list dictionary.
        """
        maker = GarmentMaker()
        order = TestOrderProcessor.create_lululime_shirtmen_order()
        maker.order_processor.order_list[1] = order
        maker.shirt_men_maker(order)
        garment = maker.garment_list.get(1)[0]
        self.assertTrue(isinstance(garment, ShirtMenLuluLime))

    def test_create_shirt_women(self):
        """
        Unit test for create_shirt_men. Asserts that the method creates
        ShirtWomen based on its order.
        """
        order_processor = OrderProcessor()
        order = TestOrderProcessor.create_pineapple_shirtwomen_order()
        factory = order_processor.get_factory(order)
        garment = factory.create_shirt_women(order)
        self.assertTrue(isinstance(garment, ShirtWomen))

    def test_shirt_women_maker(self):
        """
        Unit test for shirt_women_maker. Asserts that the method creates
        ShirtWomenPineappleRepublic and stores it in the garment_list dictionary.
        """
        maker = GarmentMaker()
        order = TestOrderProcessor.create_pineapple_shirtwomen_order()
        maker.order_processor.order_list[1] = order
        maker.shirt_women_maker(order)
        garment = maker.garment_list.get(1)[0]
        self.assertTrue(isinstance(garment, ShirtWomenPineappleRepublic))

    def test_create_socks_unisex(self):
        """
        Unit test for create_socks_unisex. Asserts that the method creates
        SockPairUnisex based on its order.
        """
        order_processor = OrderProcessor()
        order = TestOrderProcessor.create_nika_socks_order()
        factory = order_processor.get_factory(order)
        garment = factory.create_socks_unisex(order)
        self.assertTrue(isinstance(garment, SockPairUnisex))

    def test_socks_unisex_maker(self):
        """
        Unit test for socks_unisex_maker. Asserts that the method creates
        SockPairUnisexNika and stores it in the garment_list dictionary.
        """
        maker = GarmentMaker()
        order = TestOrderProcessor.create_nika_socks_order()
        maker.order_processor.order_list[1] = order
        maker.socks_unisex_maker(order)
        garment = maker.garment_list.get(1)[0]
        self.assertTrue(isinstance(garment, SockPairUnisexNika))
