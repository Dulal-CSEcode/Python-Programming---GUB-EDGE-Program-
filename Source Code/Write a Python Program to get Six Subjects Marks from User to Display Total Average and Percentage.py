marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))
marks4 = float(input("Enter marks for subject 4: "))
marks5 = float(input("Enter marks for subject 5: "))
marks6 = float(input("Enter marks for subject 6: "))

total_marks = marks1 + marks2 + marks3 + marks4 + marks5 + marks6
average_marks = total_marks / 6
percentage = (total_marks / 600) * 100

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Percentage:", percentage, "%")