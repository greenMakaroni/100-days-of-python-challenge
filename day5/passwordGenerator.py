# Day 5 final challenge: Password Generator

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""

for letter in range(0, nr_letters):
    password = password + random.choice(letters)

for symbol in range(0, nr_symbols):
    password = password + random.choice(symbols)

for number in range(0, nr_numbers):
    password = password + random.choice(numbers)
print("Easy password: ", password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

choice = []
randomized_password = ""

for letter in range(0, nr_letters):
    choice.append(random.choice(letters)) 

for symbol in range(0, nr_symbols):
    choice.append(random.choice(symbols))

for number in range(0, nr_numbers):
    choice.append(random.choice(numbers))

for character in choice:
    random_character = random.choice(choice)
    randomized_password = randomized_password + random_character
    choice.remove(random_character)

print("Randomized password: ", randomized_password)

