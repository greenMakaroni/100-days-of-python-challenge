import turtle as t
import random

t.colormode(255)
timmy = t.Turtle()
timmy.width(7)
timmy.speed("fastest")

# random rgb generator
def randomColor():
    return (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

timmy.penup()
timmy.setpos(-300, -200)

def drawPainting():
    def drawColumn():
        for i in range(1, 10):            
            timmy.color(randomColor())
            timmy.begin_fill()
            timmy.circle(10)
            timmy.end_fill()


timmy.color(randomColor())
timmy.begin_fill()
timmy.circle(10)
timmy.end_fill()

screen = t.Screen()
screen.exitonclick()
