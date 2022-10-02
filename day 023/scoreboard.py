FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-200, 230)
        self.write(arg="LEVEL 1", move=False, align="center", font=FONT)

    def updateScore(self, level):
        self.clear()
        self.write(arg=f"LEVEL {level}", move=False, align="center", font=FONT)

    def gameOver(self):
        self.goto(0,0)
        self.write(arg="Game Over", move=False, align="center", font=FONT)


