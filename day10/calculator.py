


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

repeat = True
a = 0
b = 0
operator = ""
user_choice = 'yes'

while repeat:
    user_choice = input("Do you want to perform operation? 'yes'/'no'")
    if user_choice == 'yes':
        a = int(input("Type number a "))
        operator = input("What operation to perform? ")
        b = int(input("Type number b "))
        if operator == '+':
            print(add(a, b))
        elif operator == '-':
            print(subtract(a, b))
        elif operator == '*':
            print(multiply(a, b))
        elif operator == '/':
            print(divide(a, b))
        else:
            print("Invalid operator, please try again")
    elif user_choice == 'no':
        print("Thanks for using calculator.py")
        repeat = False
    else:
        print("Invalid input")