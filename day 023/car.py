from turtle import Turtle
import random

class Car(Turtle):

    def __init__(self, color, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(color)
        self.speed("fastest")
        self.goto(x=random.randint(250, 600), y=y)

    def move(self):
        if self.xcor() > -325:
            self.goto(x=self.xcor() - 5, y=self.ycor())
        else:
            self.clear()