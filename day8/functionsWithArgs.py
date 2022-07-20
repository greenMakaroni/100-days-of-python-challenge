# Review
# Create a function called greet()
# Write 3 print statements inside the function.
# Call the greet() function and run your code .
def greet():
    print("Hello")
    print("How are you")
    print("Third statement")

def greet_with_name(name):
    print("Hello ", name)
    print("How are you ", name)
    print("Third statement ", name)

greet_with_name(input("Enter your name: "))

#functions with multiple inputs
def greet_with(name, location):
    print("Hello ", name)
    print("What is it like in ", location, "?")

greet_with("Dawid", "Leicester")

#positional argument
greet_with("Leicester", "Dawid")
# Highly inappropriate

# Keyword arguments
greet_with(location="London", name="Dave")