
'''
Write a program that takes a score from the user and assigns a
grade: 90+ = "A", 80-89 = "B", 70-79 = "C", 60-69 = "D", and below
60 = "F".
'''
marks = int(input("Enter your marks: "))
print("The grade is: ")
if(marks>=90):
    print("A")
elif(marks>=80):
    print("B")
elif(marks>=70):
    print("C")
elif(marks>=60):
    print("D")
else:
    print("F")