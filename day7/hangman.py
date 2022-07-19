# Day 7: Hangman game
import random

# Step 1
word_list = ["money", "power", "game", "computer", "technology"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word
chosen_word = random.choice(word_list)

# Ask the player to guess a letter and assign their answer to a variable called guess. Make guess lowercase
single_guess = input("Guess a letter: ").lower()

print(single_guess)
# Check if the letter is in single_guess

for letter in chosen_word:
    if letter == single_guess:
        print("Match")
    else:
        print("No match")