from turtle import Turtle 

LEFT = 180
TOP_LEFT = 135
BOTTOM_LEFT = 225

RIGHT = 0
TOP_RIGHT = 45
BOTTOM_RIGHT = 315


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(x=0, y=0)
        self.x_dir = 10
        self.y_dir = 10

    def move(self):
        self.goto(self.xcor() + self.x_dir, self.ycor() + self.y_dir)

    def bounce_y(self):
        self.y_dir *= -1

    def bounce_x(self):
        self.x_dir *= -1

    def reset(self):
        self.goto(x=0, y=0)
        self.x_dir = 10
        self.y_dir = 10



