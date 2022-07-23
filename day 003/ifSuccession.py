print("\n\n\n********************* Welcome to the rollercoaster! *********************\n")
height = int(input("What is your height in cm? "))

# Price tiers
# < 12 $5
# 12 - 18 "$7"
# > 18 "12"

bill = 0;

if height >= 120:
     print("\n\n********************* You can ride the rollercoaster! *********************\n")
     age = int(input("How old are you? "))
     if age < 12:
        print("\n\n********************* Ticket for kids under 12 years old is $5\n\n")
        bill += 5
     elif age >= 12 and age <= 18:
        print("\n\n********************* Ticket for kids over 12 years old is $7\n\n")
        bill += 7
     else:
        print("\n\n********************* Ticket for adults is $12\n\n")
        bill += 12
    
     wantPhoto = input("Do you want to get a photo of the ride? that is extra $3 enter Y or N: ").lower()

     if wantPhoto == "y":
        bill += 3
        print(f"Your ticket and photo together is ${bill}")
     elif wantPhoto == "n":
        print(f"Your ticket is ${bill}")
     else:
        print("You've entered incorrect value, self destruct sequence initiated")

else:
    print("********************* Sorry you cannot ride the rollercoaster *********************")   




