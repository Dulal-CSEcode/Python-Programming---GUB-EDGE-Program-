
a,b,c = map(int,input("Input three numbers: ").split())
print(a,b,c)
print("The maximum value is : ")
if(a>=b and a>=c):
    print(a," a is bigger than above three numbers.")
elif(b>=c):
    print(b," b is  bigger than above three numbers.")
else:
    print(c," c is bigger than above three numbers.")