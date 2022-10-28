from turtle import Turtle

class Text(Turtle):
    def __init__(self, name, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(float(x), float(y))
        self.write(arg=name, move=False, align="center", font=('arial black', 16, 'normal'))