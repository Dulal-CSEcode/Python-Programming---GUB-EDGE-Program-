students = {
    'Dulal': {'age': 20, 'marks': 95},
    'Hossain': {'age': 17, 'marks': 92},
    'Mim': {'age': 19, 'marks': 88},
    'Shikha': {'age': 22, 'marks': 97}
}

student_name = input("Enter the student's name: ")

if student_name in students:
    age = students[student_name]['age']
    marks = students[student_name]['marks']

    if age >= 18 and 90 < marks < 100:
        print(f"{student_name} is selected!")
    else:
        print(f"{student_name} is not selected.")
else:
    print("Student not found.")