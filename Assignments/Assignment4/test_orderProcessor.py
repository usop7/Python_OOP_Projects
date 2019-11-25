from unittest import TestCase
from garment_factory import GarmentMaker
from garment_factory import OrderProcessor
from garment_factory import Order
from garment_factory import LululimeFactory
from garment_factory import ShirtMenLuluLime


class TestOrderProcessor(TestCase):

    @staticmethod
    def create_order():
        """
        Creates a dictionary object, and loads the file into it.
        :return: Dictionary
        """
        return Order(order_number="1", date="Friday November 16 2019",
                     brand="Lululime", garment="ShirtMen", count="3",
                     style="Bowen", size="M", colour="Grey",
                     textile="Merino wool",
                     sport="Yoga", num_hidden_pockets="1")

    @staticmethod
    def create_garment_maker():
        """
        Creates a dictionary object, and loads the file into it.
        :return: Dictionary
        """
        garment_maker = GarmentMaker()
        order = TestOrderProcessor.create_order()
        garment_maker.order_processor.order_list[0] = order
        return garment_maker

    def test_get_factory(self):
        """
        Unit test for get_factory. Asserts that the method returns
        LululimeFacotry when the order's brandtype is Lululime.
        """
        order_processor = OrderProcessor()
        order = TestOrderProcessor.create_order()
        factory = order_processor.get_factory(order)
        self.assertTrue(isinstance(factory, LululimeFactory))

    def test_create_shirt_men(self):
        """
        Unit test for create_shirt_men. Asserts that the method creates
        ShirtMenLuluLime based on its order.
        """
        order_processor = OrderProcessor()
        order = TestOrderProcessor.create_order()
        factory = order_processor.get_factory(order)
        garment = factory.create_shirt_men(order)
        self.assertTrue(isinstance(garment, ShirtMenLuluLime))

    def test_shirt_men_maker(self):
        """
        Unit test for shirt_men_maker. Asserts that the method creates
        ShirtMenLuluLime and stores it in the garment_list dictionary.
        """
        maker = GarmentMaker()
        order = TestOrderProcessor.create_order()
        maker.order_processor.order_list[1] = order
        maker.shirt_men_maker(order)
        garment = maker.garment_list.get(1)[0]
        self.assertTrue(isinstance(garment, ShirtMenLuluLime))
