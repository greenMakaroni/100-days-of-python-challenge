# Coding exercise: write a program that will pick a person at random, that person will have to pay the bill
import random

names_string = input("Give me everybody's names, separated by a comma ,")

names = names_string.split(",")

print(names[random.randint(0, len(names))] + " pays the bill tonight")