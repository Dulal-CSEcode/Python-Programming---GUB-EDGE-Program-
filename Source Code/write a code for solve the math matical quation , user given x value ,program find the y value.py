def solve_equation(x):

  y = 2 * (x**2) + 5*x - 3
  return y

if __name__ == "__main__":
  try:
    x_value = float(input("Enter the value of x: "))
    y_value = solve_equation(x_value)
    print(f"For x = {x_value}, y = {y_value}")
  except ValueError:
    print("Invalid input. Please enter a valid number for x.")