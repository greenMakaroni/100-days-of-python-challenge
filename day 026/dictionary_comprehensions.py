# Dictionary comprehension

# new_dict = { new_key:new_value for item in list }

import random
names = ['Alex', 'Beth', 'Caroline', 'Dawid', 'Buzuamlak', 'Archie', 'Luke', 'Batu']

student_scores = { student:random.randint(0, 100) for student in names }
print(student_scores)

# I wrote it in 15sec and it worked the first time. I still cannot believe it.
students_who_passed = { student:student_scores[f"{student}"] for student in student_scores if student_scores[f"{student}"] > 30 }
print(students_who_passed)
