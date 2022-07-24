#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from asciLogo import art
import random
print(art)

computer_choice = random.randint(1, 101)
player_lives = 0
player_guess = -1

print("\n Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty_level = input("\nChoose a difficulty. Type 'easy' or 'hard': ")

if difficulty_level == 'easy':
    player_lives += 10
elif difficulty_level == 'hard':
    player_lives += 5
else: 
    print("Incorrect value")
    exit()


while player_lives > 0:
    print(f"Number of guesses: {player_lives}")
    player_guess = int(input("Make a guess: "))
    if player_guess == computer_choice:
        print(f"Congratulations you win {computer_choice}")
        exit()
    elif player_guess > computer_choice:
        print("Too high.")
        if (player_lives - 1) != 0:
            print("Guess again.")
            player_lives -= 1
        else:
            print(f"You lose")
            exit()
    elif player_lives < computer_choice:
        print("Too low.")
        if (player_lives - 1) != 0:
            print("Guess again.")
            player_lives -= 1
        else:
            print(f"You lose")
            exit()


