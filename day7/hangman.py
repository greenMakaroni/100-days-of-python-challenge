# Day 7: Hangman game
import random

lives = 6

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["money", "power", "game", "computer", "technology"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word
chosen_word = random.choice(word_list)
display = []
# display list 
for letter in chosen_word:
    display.append("_")

def takeAguess():
    global lives
    # Ask the player to guess a letter and assign their answer to a variable called guess. Make guess lowercase
    single_guess = input("Guess a letter: ").lower()
    wrong_guess = True

    # Check if the letter is in single_guess
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == single_guess:
            display[position] = letter
            wrong_guess = False
        else:
            continue

    if wrong_guess:
        lives -= 1
    print(display)
    print("Lives: ", lives)

def isCharInList():
    if "_" in display:
        return True
    else:
        return False

while isCharInList():
    print(stages[lives])
    if not lives == 0:
        takeAguess()
    else:
        print("You lose")
        exit()

if not isCharInList():
    print("You win")




