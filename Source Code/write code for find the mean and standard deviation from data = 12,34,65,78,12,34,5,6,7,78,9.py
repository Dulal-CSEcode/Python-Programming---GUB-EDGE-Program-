import math

def calculate_mean_std(data):
    n = len(data)
    if n == 0:
        return 0, 0  # Handle empty data case

    mean = sum(data) / n
    variance = sum([(x - mean) ** 2 for x in data]) / n
    std_dev = math.sqrt(variance)
    return mean, std_dev

data = [4, 3, 2, 5, 23, 3, 6]
mean, std_dev = calculate_mean_std(data)
print(f"Mean: {mean}")
print(f"Standard Deviation: {std_dev}")
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])