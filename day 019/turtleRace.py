from turtle import Turtle, Screen
import random

screen = Screen()
screen.listen()

colors = ["yellow", "red", "blue", "green", "orange"]
turtles = []
turtleSpeed = [50, 150, 200, 250, 300]
isWinner = False

xpos = -300
ypos = -200

for _ in range(5):
    newTurtle = Turtle("turtle")
    newTurtle.color(colors[_])
    newTurtle.up()
    newTurtle.setpos(xpos, ypos)
    turtles.append(
        newTurtle
    )
    ypos += 40

def race():
    global isWinner

    for turtle in turtles:
        turtle.forward(random.choice(turtleSpeed))
        if turtle.xcor() >= 300:
            isWinner = True
            if turtle.color() == user_bet:
                print("GG you win")
            else:
                print("Your bet was incorrect sorry better luck next time")


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? enter a color:\n yellow, red, blue, green or orange")


while not isWinner:
    race()




screen.exitonclick()