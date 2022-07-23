# Day 3 Final Challenge Project

# ********************** TREASURE ISLAND *******************************
# cli based game

print("\n\n\n********************** TREASURE ISLAND *******************************\n\n\n")
print(" Welcome to the treasure Island!\n Your mission is to find the treasure!\n\n\n")

leftOrRight = input("You're standing at a crossroads, you have two options:\n\n Type 'right' to go right\n Type 'left' to go left\n: ").lower()

if leftOrRight == "right":
    print("\n\nThis path has led you straight into bandit's trap, you fought well but there was simply too many of them")
    print(" YOU DIED ")
    print(" GAME OVER ")
    exit()
elif leftOrRight == "left":
    swimOrWait = input('''\n\nThis path has led you to a river, 
there is a castle on the other side and it looks like it may hold a treasure
the only problem is that the bridge is destroyed, your only options are to swim or wait.\n
Type 'swim' to swim
Type 'wait' to wait
: \n\n''').lower()
    if swimOrWait == "swim":
        print("\n\nThe current was not strong however you were attacked by an aligator... it took hold of your leg and dragged you to the bottom of the river")
        print(" YOU DIED ")
        print(" GAME OVER ")
        exit()
    elif swimOrWait == "wait":
        redBlueYellow = input(''' \n\nAfter waiting couple of minutes a fisherman appeared swimming down the river
        he agreed to give you a lift to the other side for the small share of the treasure,
        When approaching the castle you noticed that its abandoned and the gates are open,
        you've been wandering for a while now and you've come to a chamber with three closed doors
        red, yellow and blue.\n
        Type 'red' to cross the red door
        Type 'yellow' to cross the yellow door
        Type 'blue' to cross the blue door 
        : ''').lower()
        if redBlueYellow == "blue" or redBlueYellow == "red":
            print(''' \n\nAn army of undead skeletons was waiting on the other side, armed with swords and clubs,
            poor souls that used to live here in the times of ancient kingdom, all trappen in an enchantement which was cast by dark mage of the past
            you simply didn't stood a chance....''')
            print("YOU DIED")
            print("GAME OVER")
            exit()
        elif redBlueYellow == "yellow":
            print("\n\n************************* WINNER WINNER CHICKEN DINNER *************************")
            print('''
*******************************************************************************
        |                   |                  |                     |
_________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
        |                `"=._o`"=._      _`"=._                     |
_________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
        |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
_________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
            exit()
        else: 
            print("No cheating!!!")
            exit()
    else: 
        print("No cheating!!!")
        exit()
else:
    print("No cheating!!!")
    exit()