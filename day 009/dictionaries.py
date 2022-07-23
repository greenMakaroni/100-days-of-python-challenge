# Dictionaries are like json objects

# { key: value }

dictionary = { 
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again"
    }

print("\n Dictionary: \n")
for key in dictionary:
    print(f"{key} : {dictionary[key]}")

dictionary["Variable"] = "You can think of it as a box in which you can store any piece of data or executable code"

print("\n Add to dictionary: \n ")
for key in dictionary:
    print(f"{key} : {dictionary[key]}")

# Create empty dictionary
empty_dictionary = {}

print("\nEmpty dictionary: \n", empty_dictionary)

# Wipe an existing dictionary
dictionary = {}
print("\n Wipe dictionary: \n", dictionary)

