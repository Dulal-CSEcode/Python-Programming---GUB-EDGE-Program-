marks = int(input("Enter your marks: "))
print("The grade is: ")
match marks:
    case marks if marks>=90:
        print("A")
    case marks if marks>=80:
        print("B")
    case marks if marks>=70:
        print("C")
    case marks if marks>=60:
        print("D")
    case _:
        print("Fail")