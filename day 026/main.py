 # List comprehensions

numbers = [1, 2, 3]

#new_list = []
#for n in numbers:
#   add_1 = n + 1
#    new_list.append(add_1)

# 4 lines of code become 1
new_list = [number + 1 for number in numbers]
print(new_list) # output [2, 3, 4]

name = "dawid"
char_list = [letter for letter in name]
print(char_list) # output ['d','a','w','i','d']

number_range = range(1,5)
new_range = [number * 2 for number in number_range]
print(new_range) # output [2, 4, 6, 8]

list_of_names = ['Alex', 'Beth', 'Dave', 'Freddie', 'Max']
four_letter_names = [name for name in list_of_names if len(name) == 4]
print(four_letter_names) # output ['Alex', 'Beth', 'Dave']

upper_case_names = [name.upper() for name in list_of_names if len(name) > 5]
print(upper_case_names) # output ['FREDDIE']


