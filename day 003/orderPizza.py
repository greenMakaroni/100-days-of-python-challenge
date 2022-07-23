# Exercise: Order Pizza program

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza : $25

# Pepperoni for small pizza: + $2
# Pepperoni for medium or large pizza: + $3
#Extra cheese for any size pizza: + $1

print("\n\n\n************** Welcome to PizzaBoot can I take your order? *******************\n\n\n")

bill = 0
pepperoni_cost = 0

size = input("What size of pizza would you like? \n Enter:\n S for small $15\n M for medium $20\n L for large $25\n:").lower()

if size == "s":
    bill += 15
    pepperoni_cost += 2
elif size == "m":
    bill += 20
    pepperoni_cost += 3
elif size == "l":
    bill += 25
    pepperoni_cost += 3
else:
    print("Incorrect value.")
    exit()

extra_pepperoni = input("\n\nDo you want extra pepperoni for your pizza?\n Enter:\n Y for Yes\n N for No\n: ").lower()

if extra_pepperoni == "y":
    bill += pepperoni_cost
elif extra_pepperoni != "n":
    print("Incorrect value.")
    exit()

extra_cheese = input("\n\nDo you want extra cheese for your pizza?\n Enter:\n Y for yes\n N for No\n: ").lower()

if extra_cheese == "y":
    bill += 1
elif extra_cheese != "n":
    print("Incorrect value.")
    exit()

print(f"Your bill is ${bill}")



