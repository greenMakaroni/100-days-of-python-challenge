# scope & namespace

# Global scope, variables available throughout entire file
variable = 1
second_variable = 5

def increase_variable():
    variable = 2
    print(f"Variable INSIDE function: {variable}")

# global keyword informs function that second_variable comes from global scope
def increase_second_variable():
    global second_variable
    second_variable = 10
    print(f"Second variable INSIDE function with global keyword: {second_variable}")

increase_variable()
increase_second_variable()

print(f"Variable OUTSIDE function: {variable}")
print(f"Second variable OUTSIDE function with global keyword: {second_variable}")

# instead of modifying variable with global you can just return it instead
def return_second_variable():
    return second_variable + 15

second_variable = return_second_variable()
print(f"Returning second variable: {second_variable}")

# local scope
def some_function():
    function_variable = 5
    print(function_variable)

some_function()

#Statement below results in error because it was called outside its scope, 
#print(function_variable)

#Traceback (most recent call last):
#   File "C:\Users\mrtnd\Desktop\100-days-python-challenge\day 012\scope.py", line 30, in <module>
#     print(function_variable)
# NameError: name 'function_variable' is not defined

# this is local variable and the scope is limited only to the function block where it was declared

# However there's no block scope in python
if True:
    no_block_scope = 12

print(no_block_scope)

# Stuff inside if statements, loops, switches blocks have the scopes of their enclosing functions or global scope if declared outside
enemies = ["Skeleton", "Zombie", "Alien"]

if True:
    new_enemy = enemies[0]

print(new_enemy)

# Global constants, the convention is to use all upper case 
# for constant variables that you don't ever change

PI = 3.14159
URL = "https://www.google.com"

print(f"pi: {PI}, url: {URL}")



