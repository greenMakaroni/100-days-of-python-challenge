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
scoreboard = Scoreboard()
player = Player()

# game vars
game_is_on = True
FINISH_LINE_Y = 280

# Event handlers
screen.onkey(key="Up", fun=player.move)

#spawn 12 cars
for _ in range(20):
    car_manager.spawnCar()

def levelUp():
    if player.ycor() >= FINISH_LINE_Y:
        car_manager.levelUp()
        player.levelUp()
        scoreboard.updateScore(player.score)

def detect_collision():
    for car in car_manager.cars:
        if player.xcor() <= car.xcor() + 30 and player.xcor() >= car.xcor() - 30:
            if player.ycor() <= car.ycor() + 20 and player.ycor() >= car.ycor() - 20:
                car_manager.stopCars()
                player.stopPlayer()
                scoreboard.gameOver()

while game_is_on:
    time.sleep(0.03)
 
    car_manager.moveCars()
    detect_collision()
    levelUp()

    screen.update()
