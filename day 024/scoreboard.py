from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 250)
        self.score = 0
        self.high_score = 0
        self.write(arg=f"SCORE: 0 / HIGH SCORE: {self.high_score}", move=False, align="center", font=('arial black', '16', 'normal'))

    def updateScoreboard(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score} / HIGH SCORE: {self.high_score}", move=False, align="center", font=('arial black', '16', 'normal'))

    def drawGameOver(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align="center", font=('arial black', '22', 'normal'))

    def setScore(self):
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.updateScoreboard()



        
