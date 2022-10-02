from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        self.speed("fastest")
        self.goto(x=random.randint(325, 900), y=random.randint(-220, 290))
        self.MOVE_SPEED = 5

    def move(self):
        if self.xcor() > -325:
            self.goto(x=self.xcor() - self.MOVE_SPEED, y=self.ycor())
        else:
            self.goto(x=random.randint(325, 900), y=random.randint(-220, 290))

    def getSpeed(self):
        return self.MOVE_SPEED
        
    def setSpeed(self, speed):
        self.MOVE_SPEED = speed
