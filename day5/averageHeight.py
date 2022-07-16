# Coding exercise: write a program that will print an average height out of list of student heights
# COMPLETE CHALLENGE WITHOUT USING len() and sum() functions !!!!!!!!!!!!!
 
# Don't change the code below 
student_heights = input("Input a list of student heights").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# Don't change the code above


# Write your code here
sum_heights = 0
number_of_students = 0
average_height = 0

for height in student_heights:
    sum_heights += height
    number_of_students += 1

average_height = round(sum_heights / number_of_students)

print("The average height equals: ", average_height)
