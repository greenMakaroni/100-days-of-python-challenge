print("\n\n\n********************* Welcome to the rollercoaster! *********************\n")
height = int(input("What is your height in cm? "))


if height >= 120:
    print("\n\n********************* You can ride the rollercoaster! *********************\n")
    age = int(input("How old are you? "))
    if age <= 18:
        print("\n\n ********************* The ticket for 18 year olds or under is $7  *********************")
    else:
        print("The ticket for over 18 year olds is $12")
else:
    print("You CANNOT ride the rollercoaster")