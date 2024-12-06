
num = int(input("Enter a number: "))
match num:
    case  num if num<0:
        print("Negative")
    case num if num>0:
        print("Positive")
    case _:
        print("Zero")