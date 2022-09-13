from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 250)
        self.write("Score: 0", False, align="center", font=('arial black', '22', 'normal'))

    def updateScoreboard(self, score):
        self.clear()
        self.write(f"Score: {score}", False, align="center", font=('arial black', '22', 'normal'))



        
