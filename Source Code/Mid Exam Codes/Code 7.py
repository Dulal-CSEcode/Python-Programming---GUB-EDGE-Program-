from statistics import mean, median, mode
numbers = list(map(float, input("Enter space-separated numbers: ").split()))
print("Mean:", mean(numbers))
print("Median:", median(numbers))
try:
    print("Mode:", mode(numbers))
except:
    print("No unique mode found")