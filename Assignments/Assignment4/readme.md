# Garment Factory

Garment Factory is a simple console app that reads orders from an excel file, and produces garments based on its Brand type by using factory design pattern.

## Entry Point

* garment_factory.py

## Work Process

- When creating a GarmentMaker object, an OrderProcessor will be instantiated and assigned as its attribute.
- OrderProcessor is responsible for opening and reading an excel file.
  - Each row will be converted to an Order object that holds order details, and stored in the order_list dictionary as {order number: order object}
- GarmentMaker will iterate each Order in the OrderProcessor's order_list and will call a corresponding method* based on its garment type
  - *shirt_men_maker, shirt_women_maker, socks_unisex_maker
  - OrderProcessor's get_factory method will be used to call a corresponding BrandFactory
  - Produced garments will be stored in 'garment_list' dictionary as {order number: a list of garments}
- GarmentMaker will generate a report that contains a single line per order that includes a brand, a garment type, and a list of garments.



## Answers to the questions

- (Q1) For new off-brand Goosie:
  - add 'BrandEnum' GOOSIE of "Goosie"

  - create three classes that implements each garment interface like below:

    - ShirtMenGoosie(ShirtMen)
    - ShirtWomenGoosie(ShirtWomen)
    - SockPairUnisexGoosie(SockPairUnisex)

  - create 'GoosieFactory(BrandFactory)' class that implements the BrandFactory interface: it will have the following three methods:

    - create_shirt_men(self, order: Order) -> ShirtMenGoosie
    - create_shirt_women(self, order: Order) -> ShirtWomenGoosie
    - create_socks_unisex(self, order: Order) -> SockPairUnisexGoosie

  - add 'GOOSIE' brand type in OrderProcessor's brand_map dictionary so that its get_factory(Order) can return GoosieFactory:
    {BrandEnum.GOOSIE: GoosieFactory}

- (Q2) For new garment type Women's activewear pants for each of the three brands:
  - add 'GarmentEnum' ACTIVEWEAR_WOMEN of "ActiveWearWomen"
  - create 'ActiveWearWomen' interface.
  - create three child classes of 'ActiveWearWomen' interface for each brand:
    -  ActiveWearWomenLuluLime(ActiveWearWomen), 
    -  ActiveWearWomenPineappleRepublic(ActiveWearWomen) 
    -  ActiveWearWomenNika(ActiveWearWomen)
  - create 'create_activewear_women(self, order: Order) -> ActiveWearWomen' method in BrandFactory interface and all the concrete brand's factories.
  - create 'activewear_women_maker(self, order: Order)' method in GarmentMaker that uses BrandFactory's 'create_activewear_women' method.
  - add 'ACTIVEWEAR_WOMEN' garment type in GarmentMaker's garment_map dictionary so that each order can be mapped to a corresponding garment maker methods:
    {GarmentEnum.ACTIVEWEAR_WOMEN: self.activewear_women_maker}
