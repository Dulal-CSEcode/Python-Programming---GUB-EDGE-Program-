import cmath

def solve_quadratic_equation(a, b, c, d):
  # Calculate the discriminant
  delta = (b**2) - 4*(a*c)

  # Find two solutions
  if delta >= 0:
    x1 = (-b - delta**0.5) / (2*a)
    x2 = (-b + delta**0.5) / (2*a)
  else:
    x1 = (-b - cmath.sqrt(delta)) / (2 * a)
    x2 = (-b + cmath.sqrt(delta)) / (2 * a)

  print(f"Solutions for the equation {a}x^2 + {b}x + {c} = {d}:")
  print(f"x1 = {x1}")
  print(f"x2 = {x2}")


if __name__ == "__main__":
  try:
    a = float(input("Enter the coefficient 'a': "))
    b = float(input("Enter the coefficient 'b': "))
    c = float(input("Enter the coefficient 'c': "))
    d = float(input("Enter the value 'd': "))

    solve_quadratic_equation(a, b, c-d, 0) #Transform to ax^2 + bx + c = 0

  except ValueError:
    print("Invalid input. Please enter valid numbers for coefficients.")