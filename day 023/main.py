import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Frogger")
screen.tracer(0)
screen.listen()

# game objects
car_manager = CarManager()
player = Player()

# game vars
car_manager.spawnWave()
game_is_on = True

# Event handlers

screen.onkey(key="Up", fun=player.move)

while game_is_on:
    time.sleep(0.1)

    car_manager.moveCars()


    screen.update()
