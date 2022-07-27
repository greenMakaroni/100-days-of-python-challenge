from art import logo, vs
import random
from game_data import data
import os
clear = lambda: os.system('cls')

print(logo)

def printSubjectsToCompare(first, second):
        print(f"Compare: {first['name']}, {first['description']}\n")
        print(vs)
        print(f"Against: {second['name']}, {second['description']}\n")

def game():
    score = 0
    alive = True
    compare_first = random.choice(data)
    compare_second = random.choice(data)
    while compare_first == compare_second:
        compare_second = random.choice(data)

    while alive:
        print(f"Your score is: {score}")
        printSubjectsToCompare(first=compare_first, second=compare_second)
        user_guess = input("Who has more followers? type 'A' or 'B': ").upper()
        
        if user_guess == 'A' and compare_first['follower_count'] > compare_second['follower_count']:
            score += 1
            compare_first = compare_second
            compare_second = random.choice(data)
            while compare_first == compare_second:
                compare_second = random.choice(data)
        elif user_guess == 'B' and compare_first['follower_count'] < compare_second['follower_count']:
            score += 1
            compare_second = compare_first
            compare_first = random.choice(data)
            while compare_first == compare_second:
                compare_second = random.choice(data)
        elif user_guess != 'A' and user_guess != 'B':
            clear()
            print("Incorrect value, please try again")
        else:
            clear()
            alive = False
            print(f"Incorrect, you lose! Your score is: {score}.")

game()