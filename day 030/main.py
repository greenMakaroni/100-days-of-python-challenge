# FileNotFound
#       with open("a_file.txt") as file:
#           file.read()

# KeyError
#       a_dictionary = {"key":"value"}
#       value = a_dictionary["wrong_key"]

# IndexError
#       fruit_list = ["Apple", "Banana", "Pear"]
#       fruit = fruit_list[3]

# TypeError
#       text = "abc"
#       print(text + 5)
# Murphy's law

# Exception Handling
# try   -> try to do something
# except -> this block executes when something went wrong in try block
# else -> do this if there were no exceptions
# finally -> do this no matter what happens

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height shouldn't be more than 3 meters buddy...")

bmi = weight / height ** 2

try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    print("There was an error!")
    file = open("a_file.txt", "w")
except KeyError as error_message:
    print(f"The key {error_message} does not exist!")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    raise TypeError("This is an error I made up")