from turtle import Turtle

class Score(Turtle):

    def __init__(self, x):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x, 250)
        self.write(arg=f"{self.score}", move=False, align="center", font=('arial black', '22', 'normal'))

    def updateScore(self, score):
        self.clear()
        self.write(arg=f"{score}", move=False, align="center", font=('arial black', '22', 'normal'))