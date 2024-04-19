# structure of list comprehension
# new_list = [new_item for old_item in old_list]

# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)


# list2 = [i * 2 for i in range(1, 6)]
# print(list2)

# names = ["Alex", "Beth", "Eleanor", "Caroline", "Freddie", "Dave"]
# short_names = [i for i in names if len(i) <= 4]  # using if check
# print(short_names)
# capit_long_names = [i.upper() for i in names if len(i) > 4]
# print(capit_long_names)


# dictionary comprehension
# Structure: new_dict = {new_key:new_value for (key, value) in dict.items() if test}
import random
import pandas

# random.seed(42)
# names = ["Alex", "Greta", "Vova", "Marci", "Doyle"]
# student_scores = {student: random.randint(1, 100) for student in names}
# print(f"All students: {student_scores}")
# passed_students = {
#     student: score for (student, score) in student_scores.items() if score > 60
# }
# print(f"Passed: {passed_students}")
student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 78, 90]}
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
# For looping throgh rows of a dataframe we use iterrows():
for index, row in student_data_frame.iterrows():
    print(row.student)
