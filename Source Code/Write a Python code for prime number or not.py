import math

def is_prime(num):
  pass

if __name__ == "__main__":
  try:
    number = int(input("Enter an integer: "))
    if number % 2 == 0:
      print(f"{number} is an even number.")
    else:
      print(f"{number} is an odd number.")
  except ValueError:
    print("Invalid input. Please enter a valid integer.")