from turtle import Turtle

class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 300)
        self.setheading(270)

        for i in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
            
