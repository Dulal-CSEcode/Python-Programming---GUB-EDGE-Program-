variable = input("Enter a variable: ")
try:
    eval_variable = eval(variable)
    print("Data type:", type(eval_variable))
except:
    print("Data type: string")