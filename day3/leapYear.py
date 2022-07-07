#CHALLENGE: write a program that works out if given year is a leap year
print("\n\n\nWelcome to isLeap, program that will work out if a given year is a leap year!\n\n")

year = int(input("Enter a year: "))

isLeap = f"Year {year} is a leap year"
isNotLeap = f"Year {year} is NOT a leap year!"

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(isLeap)
        else:
            print(isNotLeap)
    else:
        print(isLeap)
else:
    print(isNotLeap)