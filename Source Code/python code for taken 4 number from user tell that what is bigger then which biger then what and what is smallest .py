try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    num4 = float(input("Enter the fourth number: "))

    numbers = [num1, num2, num3, num4]
    numbers.sort()

    print(f"{numbers[3]} is bigger than {numbers[2]} which is bigger than {numbers[1]} and {numbers[0]} is the smallest.")

except ValueError:
    print("Invalid input. Please enter numeric values.")