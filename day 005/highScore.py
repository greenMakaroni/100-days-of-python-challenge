# Coding challenge highest score
# Write a program that calculates the highest score from a list of student scores
# COMPLETE CHALLENGE WITHOUT USING max() function !!!!!!!!!!!!!!!!!!!!!!!!!!

# Don't change the code below
student_scores = input("Input a list of student scores: ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# Don't change the code above

# Write your code here

highest_score = 0

for score in student_scores:
    if highest_score < score:
        highest_score = score

print("The highest score is: ", highest_score)
