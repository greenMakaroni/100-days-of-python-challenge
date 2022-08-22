# draw a square challenge

from turtle import Turtle, Screen

def drawSquare(side):
    global timmy
    timmy.forward(side)
    timmy.right(90)
    timmy.forward(side)
    timmy.right(90)
    timmy.forward(side)
    timmy.right(90)
    timmy.forward(side)
    

timmy = Turtle()
timmy.shape("turtle")
timmy.color("orange")
timmy.pencolor("black")

drawSquare(100)

screen = Screen()
screen.exitonclick()