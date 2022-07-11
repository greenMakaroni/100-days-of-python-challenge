import random

list_of_fruit = ["apple", "banana", "kiwi", "Mango"]

print("\n List of fruit: ", list_of_fruit)
print("\n First fruit from a list: " + list_of_fruit[0])
print("\n Second fruit from a list: " + list_of_fruit[1])
print("\n Last fruit from a list: " + list_of_fruit[-1])
print("\n Random fruit from a list: " + list_of_fruit[random.randint(0, 2)])


list_of_fruit.append("Orange")
print("\n Add fruit to a list: ", list_of_fruit)

list_of_vegetables = ["Carrot", "Broccoli", "Cauliflower", "Kale", "Potato"]

# nesting lists

fruits_and_vegetables = [list_of_fruit, list_of_vegetables]

print("\n List of fruit: ", list_of_fruit)
print("\n List of vegetables: ", list_of_vegetables)
print("\n Nested lists", fruits_and_vegetables)

list_of_vegetables[-1] = "Tomato"
print(list_of_vegetables)

