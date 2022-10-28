# Exercise 4 You are going to use Dictionary Comprehension to create
# a dictionary called result that takes each word as key and its length as value
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

result = {word:len(word) for word in sentence.split()}


print(result)

