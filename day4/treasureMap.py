# Coding challenge treasure map: 
# Instructions: Your program should allow you to enter the position of the treasure 
# using a two-digit system, the first digit is the horizontal column number
# and the second digit is the vertical row number

# Don't change the code below 
row1 = ["🕳","🕳","🕳"]
row2 = ["🕳","🕳","🕳"]
row3 = ["🕳","🕳","🕳"]

map = [row1, row2, row3]

print("   1   2   3")
print(f"1{row1}\n2{row2}\n3{row3}")
position = input("Where do you want to put the treasure? ")
# Don't change the code above

firstDigit = int(position[0]) -1
secondDigit = int(position[1]) -1

map[firstDigit][secondDigit] = "💎"

print("   1   2   3")
print(f"1{row1}\n2{row2}\n3{row3}")