# Classic snake game challenge
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")


snakeLength = 3
xpos = 0
ypos = 0

def snakeBody(x, y, length):
    global snakeLength

    for _ in range(length):
        segment = Turtle("square")
        segment.color("white")
        segment.setpos(x, y)
        x -= 20

snakeBody(x=xpos, y=ypos, length=snakeLength)

screen.exitonclick()