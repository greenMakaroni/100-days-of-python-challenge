from turtle import Turtle, Screen
from random import choice

colors = ["orange", "aquamarine", "brown", "red", "blue", "yellow", "green", "red"]
timmy = Turtle()

def drawShape(angle, sideLength):
    global timmy
    sides = int(360 / angle)
    for _ in range(0, angle):
        timmy.forward(sideLength)
        timmy.right(sides)
       


for i in range(3, 12):
    timmy.pencolor(choice(colors))
    drawShape(i, 100)

screen = Screen()
screen.exitonclick()