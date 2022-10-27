# exercise nr 3 print numbers which are both in file1 and file2
# Write your code above 👆

def read_file(file):
    """ Read the file and remove '\n' tag"""
    with open(file) as f:
        read_f = f.readlines()
        f = [num.replace("\n", "") for num in read_f]
        return f

file_1 = read_file("file1.txt")
file_2 = read_file("file2.txt")

result = [num for num in file_1 if num in file_2]

print(result)

# I call the variable num but it's actually a str
print(type(result[0]))