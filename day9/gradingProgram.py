student_scores = {
    "Harry": 81,
    "Ron": 65,
    "Hermione": 99,
    "Draco": 90,
    "Neville": 95,
}

# Don't change the code above

# todo: create an empty dictionary called student_grades.
# todo: write your code below to add the grades to student_grades
# Grading criteria: 

# 91-100 = "Outstanding"
# 81-90 = "Exceeds expectations"
# 71-80 = "Acceptable"
# 0 - 70 = "Fail"

student_grades = {}

for student in student_scores:
    if student_scores[student] <= 70:
        student_grades[student] = "Fail"
    elif student_scores[student] > 70 and student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
    elif student_scores[student] > 80 and student_scores[student] <= 90:
        student_grades[student] = "Exceeds expectations"
    elif student_scores[student] > 90 and student_scores[student] <= 100:
        student_grades[student] = "Outstanding"
    else:
        print("Wrong value in dictionary")
        exit()

# Don't change the code below
print("\n", student_grades, "\n")

for student in student_grades:
    print(f"{student} : {student_grades[student]}")