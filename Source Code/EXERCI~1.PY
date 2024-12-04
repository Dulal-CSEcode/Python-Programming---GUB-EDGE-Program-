
initialblance = 10000

while (1):
    withdraw = int(input("Input in your amount: "))
    initialblance = initialblance-withdraw
    if(initialblance<=0):
        print("You cant withdraw the money you blance is insufficient!!!")
        initialblance = initialblance+withdraw
        break
    else:
        print("you can withdraw money & you current blance is : ",initialblance)
