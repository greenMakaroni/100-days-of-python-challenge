# Coding challenge:
# Add even numbers challenge
# Write a program that calculates the sum of all the even numbers from 1 to 100, including 1 and 100

sum_of_evens = 0

for number in range(0, 101, 2):
    sum_of_evens += number

print("Sum of even numbers between 1 and 100 is equal to: ", sum_of_evens)
