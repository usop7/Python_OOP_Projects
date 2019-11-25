from unittest import TestCase
from garment_factory import GarmentMaker, OrderProcessor, Order, \
    LululimeFactory, PineappleRepublicFactory, NikaFactory, ShirtMenLuluLime, \
    ShirtWomenPineappleRepublic, ShirtMen, ShirtWomen, SockPairUnisex, \
    SockPairUnisexNika


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

    def test_get_lululime_factory(self):
        """
        Unit test for get_factory. Asserts that the method returns
        LululimeFacotry when the order's brand is Lululime.
        """
        order_processor = OrderProcessor()
        order = TestOrderProcessor.create_lululime_shirtmen_order()
        factory = order_processor.get_factory(order)
        self.assertTrue(isinstance(factory, LululimeFactory))

    def test_get_pineapple_factory(self):
        """
        Unit test for get_factory method. Asserts that the method returns
        PineappleRepublicFactory when the order's brand is PineappleRepublic.
        """
        order_processor = OrderProcessor()
        order = TestOrderProcessor.create_pineapple_shirtwomen_order()
        factory = order_processor.get_factory(order)
        self.assertTrue(isinstance(factory, PineappleRepublicFactory))

    def test_get_nika_factory(self):
        """
        Unit test for get_factory method. Asserts that the method returns
        NikaFactory when the order's brand is Nika.
        """
        order_processor = OrderProcessor()
        order = TestOrderProcessor.create_nika_socks_order()
        factory = order_processor.get_factory(order)
        self.assertTrue(isinstance(factory, NikaFactory))

    def test_create_shirt_men(self):
        """
        Unit test for create_shirt_men method. Asserts that the method creates
        ShirtMen based on its order.
        """
        order_processor = OrderProcessor()
        order = TestOrderProcessor.create_lululime_shirtmen_order()
        factory = order_processor.get_factory(order)
        garment = factory.create_shirt_men(order)
        self.assertIsInstance(garment, ShirtMen)

    def test_shirt_men_maker(self):
        """
        Unit test for shirt_men_maker method. Asserts that the method creates
        ShirtMenLuluLime and stores it in the garment_list dictionary.
        """
        maker = GarmentMaker()
        order = TestOrderProcessor.create_lululime_shirtmen_order()
        maker.order_processor.order_list[1] = order
        maker.shirt_men_maker(order)
        garment = maker.garment_list.get(1)[0]
        self.assertIsInstance(garment, ShirtMenLuluLime)

    def test_create_shirt_women(self):
        """
        Unit test for create_shirt_women method. Asserts that the method
        creates ShirtWomen based on its order.
        """
        order_processor = OrderProcessor()
        order = TestOrderProcessor.create_pineapple_shirtwomen_order()
        factory = order_processor.get_factory(order)
        garment = factory.create_shirt_women(order)
        self.assertIsInstance(garment, ShirtWomen)

    def test_shirt_women_maker(self):
        """
        Unit test for shirt_women_maker  method. Asserts that the method creates
        ShirtWomenPineappleRepublic and stores it in the garment_list dictionary.
        """
        maker = GarmentMaker()
        order = TestOrderProcessor.create_pineapple_shirtwomen_order()
        maker.order_processor.order_list[1] = order
        maker.shirt_women_maker(order)
        garment = maker.garment_list.get(1)[0]
        self.assertIsInstance(garment, ShirtWomenPineappleRepublic)

    def test_create_socks_unisex(self):
        """
        Unit test for create_socks_unisex method. Asserts that the method
        creates SockPairUnisex based on its order.
        """
        order_processor = OrderProcessor()
        order = TestOrderProcessor.create_nika_socks_order()
        factory = order_processor.get_factory(order)
        garment = factory.create_socks_unisex(order)
        self.assertIsInstance(garment, SockPairUnisex)

    def test_socks_unisex_maker(self):
        """
        Unit test for socks_unisex_maker method. Asserts that the method creates
        SockPairUnisexNika and stores it in the garment_list dictionary.
        """
        maker = GarmentMaker()
        order = TestOrderProcessor.create_nika_socks_order()
        maker.order_processor.order_list[1] = order
        maker.socks_unisex_maker(order)
        garment = maker.garment_list.get(1)[0]
        self.assertIsInstance(garment, SockPairUnisexNika)
