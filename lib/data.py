from models.factory import Factory
from models.car import Car
from models.reparation import Reparation
from models.__init__ import CONN, CURSOR

def data_from_DB():
    Car.drop_table()
    Factory.drop_table()
    Reparation.drop_table()
    Reparation.create_table()
    Factory.create_table()
    Car.create_table()

    Factory.create("Honda","Japan")
    Factory.create("Toyota","Japan")
    Factory.create("Ford","USA")
    Factory.create("Dodge","USA")
    Factory.create("Chevrolet","USA")

    Car.create("Civic EX",2022,	3004.0, 1)
    Car.create("Corvette 1LT", 2023, 3366.0, 5)
    Car.create("Corvette Stingray Coupe", 2022, 3637.0, 5)
    Car.create("Mustang", 2024, 3579.0, 3)
    Car.create("Mustang Mach-E", 2023,	4394.0,	3)
    Car.create("Shelby GT500", 2022, 4183.0, 3)
    Car.create("Mustang GT", 2024, 3843.0, 3)
    Car.create("Accord EX ", 2024, 3280.0, 1)
    Car.create("Civic Type R", 2023, 3188.0, 1)
    Car.create("Insight", 2022, 3078.0, 1)
    Car.create("GR86 Coupe 2D", 2023, 2868.0, 2)
    Car.create("Avalon", 2022, 3570.0, 2)
    Car.create("Mirai", 2023, 4335.0, 2)
    Car.create("Camry XSE", 2024, 3530.0, 2)
    Car.create("Corolla LE", 2024, 3150.0, 2)
    Car.create("Charger GT", 2023, 4073.0, 4)
    Car.create("Challenger R/T", 2023, 4157.0, 4)
    Car.create("Camaro SS ", 2015, 3339.0, 5)
    Car.create("Camaro 1LT", 2023, 3684.0, 5)

data_from_DB()