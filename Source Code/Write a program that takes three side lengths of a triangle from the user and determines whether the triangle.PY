
a,b,c = map(int,input("Input three sides of a triangle: ").split())


if(a+b>c and b+c>a and a+c>b):
    print("Valid Triangle")
    if(a==b or a==c or b==c):
      print("Isosceles Triangle")
    elif(a==b and b==c and a==c):
      print("Equilateral Triangle")
    elif(a==b or a==c or b==c):
      print("Isosceles Triangle")
    else:
      print("Scalene Triangle")
else:
      print("Not valid triangle")
