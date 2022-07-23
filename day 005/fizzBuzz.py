# fizz buzz challenge
# classic 

# Write program that prints each number from 1 to 100
# if the number is divisible by 3 then instead of printing that number  print "Fizz"
# if the number is divisible by 5 then print Buzz 
# if the number is divisible both by 3 and 5 print FizzBuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)