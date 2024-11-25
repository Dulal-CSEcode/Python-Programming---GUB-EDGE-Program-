def add_two_numbers():
  """Gets two numbers from the user and prints their sum."""
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    sum = num1 + num2
    print("The sum of", num1, "and", num2, "is:", sum)
  except ValueError:
    print("Invalid input. Please enter numbers only.")

add_two_numbers()