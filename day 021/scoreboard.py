from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 250)
        self.write(arg="Score: 0", move=False, align="center", font=('arial black', '22', 'normal'))

    def updateScoreboard(self, score):
        self.clear()
        self.write(arg=f"Score: {score}", move=False, align="center", font=('arial black', '22', 'normal'))

    def drawGameOver(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align="center", font=('arial black', '22', 'normal'))



        
