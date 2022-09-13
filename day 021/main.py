from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()

# Draw turtles
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Game variables
score = 0
game_is_on = True

# Event handlers
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# Functions
def detect_collision():
    global food
    global score
    global game_is_on

    # food collision detection
    if snake.segments[0].distance(food.xcor(), food.ycor()) < 20:
        food.resetSnek()
        score += 1
        scoreboard.updateScoreboard(score)
    
    # walls collision detection
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        game_is_on = False

# Game loop
while game_is_on:
    screen.update()
    time.sleep(0.05)

    snake.move()

    # detect collisions with food
    detect_collision()



# So that window doesn't close instantly
screen.exitonclick()