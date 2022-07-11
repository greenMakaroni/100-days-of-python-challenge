import random

list_of_fruit = ["apple", "banana", "kiwi", "Mango"]

print("\nList of fruit: ", list_of_fruit)
print("\nFirst fruit from a list: " + list_of_fruit[0])
print("\nSecond fruit from a list: " + list_of_fruit[1])
print("\nLast fruit from a list: " + list_of_fruit[-1])
print("\nRandom fruit from a list: " + list_of_fruit[random.randint(0, 2)])


list_of_fruit.append("Orange")
print("\nAdd fruit to a list: ", list_of_fruit)

