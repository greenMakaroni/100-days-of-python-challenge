from logo import logo

print(logo)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operators = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

repeat = True
a = 0
b = 0

user_choice = 'yes'

while repeat:
    user_choice = input("Do you want to perform operation? 'yes'/'no'")
    if user_choice == 'yes':

        a = int(input("Type number a "))

        for operator in operators:
            print(operator)
        operator = input("What operation to perform? ")

        operation = operators[operator]

        b = int(input("Type number b "))

        print(operation(a, b))

    elif user_choice == 'no':
        print("Thanks for using calculator.py")
        repeat = False
    else:
        print("Invalid input")