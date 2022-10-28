# Exercise 4 applying list comprehensions to U.S. States game ( day 25 )

#imports
import turtle
import pandas
from text import Text
# us states image path
img = "blank_states_img.gif"

# setup screen
screen = turtle.Screen()
screen.addshape(img)
turtle.shape(img)

gameIsOn = True
guessed = 0
file = pandas.read_csv("50_states.csv")
states = file["state"]
guessed_states = []

while gameIsOn:
    screen.title(f"{guessed}/50 U.S. States")
    answer_state = screen.textinput(title="Guess the state", prompt="Can you guess another state?")

# Shorten this block of code using list comprehensions
#    if answer_state == "exit":
#       missing_states = []
#       for state in states:
#           if state not in guessed_states:
#               missing_states.append(state)
#       new_data = pandas.DataFrame(missing_states)
#       new_data.to_csv("states_to_learn.csv")
#       break

# Answer here:
    if answer_state == "exit":
        new_data = pandas.DataFrame([state for state in states if state not in guessed_states])
        new_data.to_csv("states_to_learn.csv")
        break

    for state in states:
        if answer_state == state:
            guessed_states.append(answer_state)
            row = file[file.state == answer_state]
            Text(answer_state, row.x, row.y)
            guessed += 1



