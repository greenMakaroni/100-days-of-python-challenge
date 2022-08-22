import turtle 
import random

turtle.colormode(255)
directions = [0, 90, 180, 270]

timmy = turtle.Turtle()
timmy.width(7)
timmy.speed("fastest")

# random rgb generator
def randomColor():
    return (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

def randomWalk():
    global timmy
    while True:
        timmy.setheading(random.choice(directions))
        timmy.pencolor(randomColor())
        timmy.forward(20)


randomWalk()

screen = Screen()
screen.exitonclick()