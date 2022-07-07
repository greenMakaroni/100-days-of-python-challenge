print("\n\n\n********************* Welcome to the rollercoaster! *********************\n")
height = int(input("What is your height in cm? "))

# Price tiers
# < 12 $5
# 12 - 18 "$7"
# > 18 "12"

if height >= 120:
     print("\n\n********************* You can ride the rollercoaster! *********************\n")
     age = int(input("How old are you? "))
     if age < 12:
        print("\n\n********************* Ticket for kids under 12 years old is $5")
     elif age >= 12 and age <= 18:
        print("\n\n********************* Ticket for kids over 12 years old is $7")
     else:
        print("\n\n********************* Ticket for adults is $12")
else:
    print("********************* Sorry you cannot ride the rollercoaster *********************")   





