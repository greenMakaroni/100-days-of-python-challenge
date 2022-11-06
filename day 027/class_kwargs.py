# class using **kwargs
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

# in case we didn't pass make or model when instantiating a class
# KeyError: 'model' / KeyError: 'make'
# to fix that we should use .get

# this way if the key is not in the dictionary the .get will just return 'none'
class BigCar:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GTR")
print("\nCar")
print(my_car.make)
print(my_car.model)


my_big_car = BigCar(make="Ford")
print("\nBig Car")
print(my_big_car.make)
print(my_big_car.model)