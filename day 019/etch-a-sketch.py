# Challenge: write a etch-a-sketch app using turtle

from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.listen()

def moveForwards():
    timmy.forward(20)

def moveBackwards():
    timmy.backward(10)

def rotateClockwise():
    timmy.right(20)

def rotateAnticlockwise():
    timmy.left(20)

def clearDrawing():
    timmy.reset()

screen.onkey(key="w", fun=moveForwards)
screen.onkey(key="s", fun=moveBackwards)
screen.onkey(key="d", fun=rotateClockwise)
screen.onkey(key="a", fun=rotateAnticlockwise)
screen.onkey(key="c", fun=clearDrawing)

screen.exitonclick()