# Exercise: ask user for single two-digit number
# add both digit of this number to create new number 
# print new number

twoDigitNumber = input("Type in 2 digit number : ")
firstDigit = twoDigitNumber[0]
secondDigit = twoDigitNumber[1]

print("first digit: ", firstDigit)
print("second digit: ", secondDigit)

print("first digit + second digit = ", int(firstDigit) + int(secondDigit))