from turtle import Screen 
from paddle import Paddle
from ball import Ball
import time

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

# Game objects
rightPaddle = Paddle(350)
leftPaddle = Paddle(-350)
ball = Ball()
# Event handlers

# Right paddle
screen.onkey(key="Up", fun=rightPaddle.moveUp)
screen.onkey(key="Down", fun=rightPaddle.moveDown)

# Left paddle
screen.onkey(key="w", fun=leftPaddle.moveUp)
screen.onkey(key="s", fun=leftPaddle.moveDown)


# Game variables
scoreRight = 0
scoreLeft = 0
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)


screen.exitonclick()