from car import Car

class CarManager:

    def __init__(self):
        self.cars = []
        
    def spawnCar(self):
        car = Car()
        self.cars.append(car)

    def moveCars(self):
        for car in self.cars:   
            car.move()

    def levelUp(self):
         for car in self.cars:   
            car.setSpeed(car.getSpeed() + 5)

    def stopCars(self):
        for car in self.cars:
            car.setSpeed(0)

             
