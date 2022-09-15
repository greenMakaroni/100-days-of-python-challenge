from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.shapesize(4,1,1)
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(x=x, y=0)

    def moveUp(self):
        self.goto(x= self.xcor(), y=self.ycor() + 35)

    def moveDown(self):
        self.goto(x= self.xcor(), y=self.ycor() - 35)    