num_char = len(input("What is your name?"))
# print("your name has " + num_char + " characters") this code produces following error

 # File "../100-days-python-challange\day2\typeErrorCheckingConversion.py", line 2, in <module>
 # print("your name has " + num_char + " characters")
 # TypeError: can only concatenate str (not "int") to str


# check the type
print(type(num_char))

# type casting
new_num_char = str(num_char)
print(type(new_num_char))

# some more type conversions
a = 123
print('type(a): ', type(a), a)
print('type(str(a)): ', type(str(a)), str(a))
print('type(float(a)): ', type(float(a)), float(a))
print('type(bool(a)): ', type(bool(a)), bool(a))

print('70 + float("100.5"): ', 70 + float("100.5"))
print('str(70) + str(100): ', str(70) + str(100))