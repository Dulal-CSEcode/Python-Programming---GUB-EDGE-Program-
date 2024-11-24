def add(x, y):
  """Adds two numbers."""
  return x + y

def subtract(x, y):
  """Subtracts two numbers."""
  return x - y

def multiply(x, y):
  """Multiplies two numbers."""
  return x * y

def divide(x, y):
  """Divides two numbers."""
  if y == 0:
    return "Division by zero error!"
  return x / y

def modulo(x, y):
  """Calculates the modulo of two numbers."""
  if y == 0:
    return "Modulo by zero error!"
  return x % y


while True:
  print("Select operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Modulo")
  print("6. Exit")

  choice = input("Enter choice(1/2/3/4/5/6): ")

  if choice in ('1', '2', '3', '4', '5'):
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("Invalid input. Please enter numbers only.")
      continue

    if choice == '1':
      print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
      print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
      print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
      print(num1, "/", num2, "=", divide(num1, num2))

    elif choice == '5':
      print(num1, "%", num2, "=", modulo(num1, num2))

  elif choice == '6':
    break
  else:
    print("Invalid Input")