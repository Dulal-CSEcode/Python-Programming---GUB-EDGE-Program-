odd_numbers = [num for num in range(1, 21, +1) if num % 2 != 0]

even_numbers = [num for num in range(20, 0, -1) if num % 2 == 0]

combined_numbers = odd_numbers + even_numbers

total_result = 0

if odd_numbers and even_numbers:
    total_result += odd_numbers[0]
    total_result += even_numbers[0]

total_result += sum(combined_numbers)

print("Odd numbers from 1 to 20:", odd_numbers)
print("Even numbers from 20 to 1:", even_numbers)
print("Combined numbers:", combined_numbers)
print("Total result (sum of all numbers, plus first elements):", total_result)
