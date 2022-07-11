# Coding challenge treasure map: 
# Instructions: Your program should allow you to enter the position of the treasure 
# using a two-digit system, the first digit is the horizontal column number
# and the second digit is the vertical row number

# Don't change the code below 
row1 = ["🕳","🕳","🕳"]
row2 = ["🕳","🕳","🕳"]
row3 = ["🕳","🕳","🕳"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# Don't change the code above

firstDigit = int(position[0])
secondDigit = int(position[1])

map[firstDigit][secondDigit] = "💎"

print(f"{row1}\n{row2}\n{row3}")