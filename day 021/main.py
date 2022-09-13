from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()
score = 0

game_is_on = True

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

def detect_collision():
    global food
    global score
    if snake.segments[0].distance(food.xcor(), food.ycor()) < 20:
        food.resetSnek()
        score += 1
        scoreboard.updateScoreboard(score)

while game_is_on:
    screen.update()
    time.sleep(0.05)

    snake.move()

    # detect collisions with food
    detect_collision()

screen.exitonclick()