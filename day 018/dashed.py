# challenge nr2 draw a dashed line

from turtle import Turtle, Screen

t = Turtle()

def drawDashedLine(dashLength):
    global t
    for _ in range(0, 20):
        t.forward(dashLength)
        t.penup()
        t.forward(dashLength)
        t.pendown()

drawDashedLine(5)


s = Screen()
s.exitonclick()