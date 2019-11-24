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

- For new off-brand Goosie:
  - add 'BrandEnum' GOOSIE of "Goosie"
  - create 'ShirtMenGoosie(ShirtMen)', 'ShirtWomenGoosie(ShirtWomen)', 'SockPairUnisexGoosie(SockPairUnisex)' classes.
  - create 'GoosieFactory' class that implements the BrandFactory interface: it will have three methods (create_shirt_men, create_shirt_women, create_socks_unisex) that return a product family of Goosie above.
  - add 'GOOSIE' brand type in OrderProcessor's brand_map dictionary so that its get_factory(Order) can return GoosieFactory.

- For new garment type Women's activewear pants for each of the three brands:
  - add 'GarmentEnum' ACTIVEWEAR_WOMEN of "ActiveWearWomen"
  - create 'ActiveWearWomen' interface.
  - create child classes of 'ActiveWearWomen' interface for the three brands:
    -  ActiveWearWomenLuluLime, ActiveWearWomenPineappleRepublic, ActiveWearWomenNika
  - add 'ACTIVEWEAR_WOMEN' garment type in GarmentMaker's garment_map dictionary so that each order can be mapped to a corresponding garment maker methods.