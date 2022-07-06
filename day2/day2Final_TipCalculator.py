print("Welcome to the tip calculator\n")

totalBill = float(input("What was the total bill? $"))
tipSize = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
numberOfPeople = int(input("How many people to split the bill? "))

totalPay = totalBill + (totalBill * (tipSize / 100))

print(f"Each person should pay ${ round(totalPay / numberOfPeople, 2) }")