start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

if start < end:
    for number in range(start, end + 1):
        print(number, end=" ")
else:
    print("Starting number should be less than the ending number.")
