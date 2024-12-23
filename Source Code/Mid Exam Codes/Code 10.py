from collections import Counter

# Read the file name
input_file = input("Enter the name of the input file (with extension): ")
output_file = input("Enter the name of the output file (with extension): ")

try:
    # Read the contents of the file
    with open(input_file, 'r') as file:
        text = file.read()

    # Count the frequency of each word
    words = text.split()
    word_count = Counter(words)

    # Write the results into the output file
    with open(output_file, 'w') as file:
        for word, count in word_count.items():
            file.write(f"{word}: {count}\n")

    print(f"Word frequencies have been saved to {output_file}.")
except FileNotFoundError:
    print("Error: The input file was not found.")