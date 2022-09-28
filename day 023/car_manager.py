from car import Car
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 15
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.waves = []
        self.car_y = 280
        
    def spawnWave(self):
        cars = []
        while self.car_y > -280:
            car = Car(random.choice(COLORS), self.car_y)
            cars.append(car)
            self.car_y -= 40
        self.car_y = 280
        self.waves.append(cars)

    def moveCars(self):
        for wave in self.waves:
            for car in wave:
                car.move()
             
