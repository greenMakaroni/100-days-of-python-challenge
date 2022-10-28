import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}


# Looping through dictionaries:

# for (key, value) in student_dict.items():
#     print(value)
#
student_data_frame = pandas.DataFrame(student_dict)
print("Student data frame\n", student_data_frame)
#
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)


# Loop through rows of data frame

for (index, row) in student_data_frame.iterrows():
    print("Index\n", index)
    print("Row\n", row)
    print("row.student\n", row.student)