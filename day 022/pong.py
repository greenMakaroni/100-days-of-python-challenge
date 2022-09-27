from turtle import Screen, right 
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

def detectCollision():
    global ball
    global rightPaddle
    global leftPaddle
    global scoreLeft
    global scoreRight
    
  # Floor and ceiling collisions
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
  # Paddle collisions
    if ball.xcor() >= rightPaddle.xcor() - 15:
        if ball.ycor() <= rightPaddle.ycor() + 50 and ball.ycor() >= rightPaddle.ycor() -50:
            ball.bounce_x()
    if ball.xcor() <= leftPaddle.xcor() + 15:
        if ball.ycor() <= leftPaddle.ycor() + 50 and ball.ycor() >= leftPaddle.ycor() -50:
            ball.bounce_x()

    if ball.xcor() > 400:
        scoreLeft += 1
        ball.reset()
        print(scoreLeft, scoreRight)
    
    if ball.xcor() < -400:
        scoreRight += 1
        ball.reset()
        print(scoreLeft, scoreRight)

   

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.05)
    detectCollision()


screen.exitonclick()