name = input("Enter your name: ")

if len(name) >= 5 and len(name) < 10 and name[0].lower() == 'a':
    print("Your name is:", name)
else:
    print("Invalid name")