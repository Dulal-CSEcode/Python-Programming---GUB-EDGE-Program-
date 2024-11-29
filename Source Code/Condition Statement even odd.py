try:
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
