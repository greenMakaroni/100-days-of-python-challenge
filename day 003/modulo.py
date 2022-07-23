# CHALLENGE: write program that will check if the number is odd or even

# Don't change the code below
number = int(input("Enter a number, program will determine if it's odd or even: "))
# Don't change the code above

if number % 2 != 0:
    print(f"The number {number} is odd")
else:
    print(f"The number {number} is even")