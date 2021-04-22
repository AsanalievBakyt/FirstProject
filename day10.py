import pprint

list = [1, 2, 3]
tuple = (1, 2, 3, 'i')
dict1 = {1, 1, 1, 1, 1, 2, 2, 3, 4, 5}

general_avg = 0
student_avg = []
std = 0
j = 0
students = [{"name": "Vova",
             "last_name": "Zinkovsky",
             "age": 17,
             "scores": [1, 2, 3, 4, 5],
             "hobbies": ['play', 'programming', 'reading']
             },
            {"name": "Begimai",
             "last_name": "Zhumakova",
             "age": 18,
             "scores": [5, 5, 3, 4, 5],
             "hobbies": ['pubg', 'programming', 'reading', 'walking']
             },
            {"name": "Aliya",
             "last_name": "Andabekova",
             "age": 18,
             "scores": [1, 4, 3, 1, 2],
             "hobbies": ['programming', 'reading', 'drawing']
             },
            {"name": "Cholpon",
             "last_name": "Kaimova",
             "age": 16,
             "scores": [5, 2, 4, 4, 5],
             "hobbies": ['pubg', 'programming', 'reading', 'anime', ]
             },
            {"name": "Bakyt",
             "last_name": "Asanaliev",
             "age": 35,
             "scores": [4, 2, 4, 4, 5],
             "hobbies": ['play', 'programming', 'reading', 'footbal', 'history']
             },
            {"name": "Maksim",
             "last_name": "Surovkin",
             "age": 22,
             "scores": [1, 1, 1, 1, 1],
             "hobbies": ['programming', 'reading', 'traveling', 'cycling']
             }
            ]

for student in students:
    sum = 0
    for score in student['scores']:
        sum += score

    a = sum / len(student['scores'])
    student_avg.append(a)
print(student_avg)
for i in student_avg:
    general_avg += i
    b = general_avg / len(student_avg)
print(b)

max_score = max(student_avg)
print(max_score)
min_score = min(student_avg)
print(min_score)
difference = max_score - min_score
print(round(difference, 2))
pprint.pprint(students)