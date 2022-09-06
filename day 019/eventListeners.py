from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.listen()

def moveForwards():
    timmy.forward(10)

# higher order function - passing function into function
screen.onkey(key="space", fun=moveForwards)
screen.exitonclick()
