from typing import List

from Person import  Person, Child
# -------------------- Composition

class Car:
    def __init__(self, regnum, brand, price, owner: Person):
        self.regnum = regnum
        self.brand = brand
        self.price = price
        self.owner = owner

    def __str__(self):
        return f"Car : {self.regnum} - Brand :{self.brand} - Price :{self.price}"

    def get_owner(self):
        return f"The owner of this car is {self.owner['age']} years old"

class Warehouse:
    def __init__(self, city, cars: List[Car]) -> None:
        self.cars = cars
        self.city = city

    def __str__(self):
        return f"{len(self.cars)} cars in {self.city} warehouse"

# -------------------------- Errors handling
    def get_mean_price(self):
        price = 0
        for car in self.cars:
            price += car.price
        if len(self.cars) == 0 :
            raise ZeroDivisionError('Division by zero impossible')
        else:
            return price/len(self.cars)


# try:
#     wh_1 = Warehouse("Nice", [])
#     wh_1.get_mean_price()
# except ZeroDivisionError as e:
#     print(e)
#     print('No cars Available')
# else:
#     print('Code to run if there is no errors')
# finally:
#     print('Code to always run')

Omar = Child.Male(15)
car_1 = Car(0o001, "Audi", "12.000 $", Omar)
car_1.get_owner()


