import turtle as t
import random

t.colormode(255)
timmy = t.Turtle()
timmy.width(4)
timmy.speed("fastest")

# random rgb generator
def randomColor():
    return (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

def drawSpirograph(circle_count):
    for _ in range(0, circle_count):
        timmy.pencolor(randomColor())
        timmy.circle(100)
        timmy.right(int(360 / circle_count))

drawSpirograph(50)

screen = t.Screen()
screen.exitonclick()




