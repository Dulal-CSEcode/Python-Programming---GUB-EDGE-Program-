try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if num1 > num2:
        print(f"{num1} is bigger than {num2}")
    elif num1 < num2:
        print(f"{num1} is smaller than {num2}")
    else:
        print("Both numbers are equal.")

except ValueError:
    print("Invalid input. Please enter numeric values.")

