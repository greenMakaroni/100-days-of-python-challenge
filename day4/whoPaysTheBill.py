# Coding exercise: write a program that will pick a person at random, that person will have to pay the bill
import random

names_string = input("Give me everybody's names, separated by a comma ,")
names = names_string.split(",")

print(names[random.randint(0, len(names) - 1) ] + " pays the bill tonight")

# alternative approach

print(random.choice(names) + " pays the bill tomorrow")