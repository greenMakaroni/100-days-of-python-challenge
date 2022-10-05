

# Read file

# open file
file = open('my_file.txt')
# read the contents save to a variable
contents = file.read()
# print contents of a file
print(contents)
# close file free-up the resources
file.close()

# Write to file
# open file in 'write' mode to overwrite all data in a file
# 'append' mode to append line to a file
with open('my_file.txt', mode="a") as file:
    file.write('new text.')

# with this approach no need to close files
with open('my_file.txt') as file:
    contents = file.read()
    print('Second approach: ', contents)

