STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.score = 1

    def move(self):
        self.forward(MOVE_DISTANCE)

    def levelUp(self):
        self.goto(STARTING_POSITION)
        self.score += 1

    def stopPlayer(self):
        global MOVE_DISTANCE
        MOVE_DISTANCE = 0
        
