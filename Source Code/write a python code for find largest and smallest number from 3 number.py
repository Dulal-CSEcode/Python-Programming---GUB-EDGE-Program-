try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    num4 = float(input("Enter the fourth number: "))

    #largest number
    if num1 >= num2 and num1 >= num3 and num1 >= num4:
        largest = num1
    elif num2 >= num1 and num2 >= num3 and num2 >= num4:
        largest = num2
    elif num3 >= num1 and num3 >= num2 and num3 >= num4:
        largest = num3
    else:
        largest = num4

    #smallest number
    if num1 <= num2 and num1 <= num3 and num1 <= num4:
        smallest = num1
    elif num2 <= num1 and num2 <= num3 and num2 <= num4:
        smallest = num2
    elif num3 <= num1 and num3 <= num2 and num3 <= num4:
        smallest = num3
    else:
        smallest = num4

    print(f"The largest number is: {largest}")
    print(f"The smallest number is: {smallest}")


    if largest == num1:
        print(f"{num1} is the largest.")
    elif largest == num2:
        print(f"{num2} is the largest.")
    elif largest == num3:
        print(f"{num3} is the largest.")
    else:
        print(f"{num4} is the largest.")

    if smallest == num1:
        print(f"{num1} is the smallest.")
    elif smallest == num2:
        print(f"{num2} is the smallest.")
    elif smallest == num3:
        print(f"{num3} is the smallest.")
    else:
        print(f"{num4} is the smallest.")

except ValueError:
    print("Invalid input. Please enter numeric values.")
