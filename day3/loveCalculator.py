# Instructions:

# You are going to write a program that tests the compatibility between two people.
# We're going to use the super scientific method recommended by BuzzFeed

# Method:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number

# For love scores less than 10 or greater than 90, the message should be:
# "Your score is x, you go together like coke and mentos"

# For love scores between 40 and 50, the message should be:
# "Your score is y, you are alright together"

# Every other case just print the score

firstDigit = 0
secondDigit = 0
score = 0

hisName = input("Enter his name: ").lower()
herName = input("Enter her name: ").lower()

firstDigit += (hisName + herName).count("t")
firstDigit += (hisName + herName).count("r")
firstDigit += (hisName + herName).count("u")
firstDigit += (hisName + herName).count("e")

secondDigit += (hisName + herName).count("l")
secondDigit += (hisName + herName).count("o")
secondDigit += (hisName + herName).count("v")
secondDigit += (hisName + herName).count("e")

score = int(str(firstDigit) + str(secondDigit))

if score < 10 or score > 90:
    print(f"Your score is { score }, you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"Your score is { score }, you are alright together")
else:
    print(f"Your score is { score }, crystal ball is confused")