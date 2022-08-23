import turtle as t
import random

t.colormode(255)
timmy = t.Turtle()
timmy.speed("fastest")

# random rgb generator
def randomColor():
    return (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

x = -300
y = -200

timmy.penup()
timmy.setpos(-300, -200)

def drawPainting():
    global x, y

    def drawColumn():
        for _ in range(1, 11):            
            timmy.color(randomColor())
            timmy.begin_fill()
            timmy.circle(10)
            timmy.end_fill()
            timmy.penup()
            timmy.forward(40)
            timmy.pendown()
    
    for _ in range(1, 11):
        y += 40
        timmy.penup()
        timmy.setpos(x, y)
        drawColumn()
    
drawPainting()



screen = t.Screen()
screen.exitonclick()
