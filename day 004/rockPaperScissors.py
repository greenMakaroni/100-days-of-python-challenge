# Day 4 final challenge:
# Instructions: create a program that will play rock paper scissors with you

import random

# Don't change code below
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

list_of_moves = [rock, paper, scissors]

userChoice = list_of_moves[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))]
computerChoice = random.choice(list_of_moves)

print("\n Your choice: \n", userChoice)
print("\n Computer choice: \n", computerChoice)

if userChoice == computerChoice:
    print("DRAW")
elif userChoice == rock and computerChoice == scissors:
    print("You win")
elif userChoice == paper and computerChoice == rock:
    print("You win")
elif userChoice == scissors and computerChoice == paper:
    print("You win")
else:
    print("Computer wins")

