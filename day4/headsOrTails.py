# coding challenge heads or tails
# instructions: You are going to write a virtual coin toss program. It will randomly tell the user
# "Heads" or "Tails".


# type code below
import random 

headsOrTails = random.randint(0, 1)

if headsOrTails == 0:
    print("Heads")
elif headsOrTails == 1:
    print("Tails")
else:
    print("Shrodinger's coin")