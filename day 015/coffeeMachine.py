MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def calculateRemainingResources(product):
    if product == 'espresso':
        resources['water'] = resources['water'] - MENU[product]['ingredients']['water']
        resources['coffee'] = resources['coffee'] - MENU[product]['ingredients']['coffee']
    else:
        resources['water'] = resources['water'] - MENU[product]['ingredients']['water']
        resources['coffee'] = resources['coffee'] - MENU[product]['ingredients']['coffee']
        resources['milk'] = resources['milk'] - MENU[product]['ingredients']['milk']

def calculateCoinValue(productPrice):
    total_value = 0
    quarters = int(input("How many quarters? "))
    total_value = total_value + (quarters / 4)

    dimes = int(input("How many dimes? "))
    total_value = total_value + (dimes / 10)

    nickles = int(input("How many nickles? "))
    total_value = total_value + (nickles / 20)

    pennies = int(input("How many pennies? "))
    total_value = total_value + (pennies / 100)

    change = total_value - productPrice
    if change < 0:
        isSufficient = False
    else:
        isSufficient = True

    return {"cost": total_value, "change": change, "sufficient": isSufficient}

def serveCoffee(user_choice):
    cost = calculateCoinValue(MENU[user_choice]["cost"])
    if cost['sufficient']:
        calculateRemainingResources(user_choice)
        print(f"Here is ${cost['change']} in change.")
        print(f"Here is your {user_choice} ☕ Enjoy!")
    else:
        print("Insufficient funds")

on = True

while on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
    elif user_choice == 'off':
        print("Thank you for using coffee machine")
        exit()
    elif user_choice != 'espresso' and user_choice != 'latte' and user_choice != 'cappuccino':
        print('incorrect input')
    else:
        if user_choice == 'espresso':
            if resources['water'] - MENU[user_choice]['ingredients']['water'] < 0:
                print("Sorry there's not enough water")
            elif resources['coffee'] - MENU[user_choice]['ingredients']['coffee'] < 0:
                print("Sorry there's not enough coffee")
            else:
                serveCoffee(user_choice)
        else:
            if resources['water'] - MENU[user_choice]['ingredients']['water'] < 0:
                print("Sorry there's not enough water")
            elif resources['coffee'] - MENU[user_choice]['ingredients']['coffee'] < 0:
                print("Sorry there's not enough coffee")
            elif resources['milk'] - MENU[user_choice]['ingredients']['milk'] < 0:
                print("Sorry there's not enough milk")
            else:
                serveCoffee(user_choice)



        



