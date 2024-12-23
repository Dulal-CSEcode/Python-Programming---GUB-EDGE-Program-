expression = input("Enter an arithmetic expression: ")
try:
    result = eval(expression)
    print("Result:", result)
except:
    print("Invalid expression")