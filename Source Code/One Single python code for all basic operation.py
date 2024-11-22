# 1. Serial Input
def get_serial_input():
    """Gets a series of numbers from the user until they enter 'done'."""
    numbers = []
    while True:
        input_value = input("Enter a number (or 'done' to finish): ")
        if input_value.lower() == 'done':
            break
        try:
            number = float(input_value)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    return numbers

# 2. Fibonacci Sequence
def fibonacci(n):
    """Generates the Fibonacci sequence up to n terms."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()

# 3. Greatest Common Divisor (GCD)
def gcd(a, b):
    """Calculates the greatest common divisor of two numbers."""
    while b:
        a, b = b, a % b
    return a

# 4. Least Common Multiple (LCM)
def lcm(a, b):
    """Calculates the least common multiple of two numbers."""
    return (a * b) // gcd(a, b)

# 5. Prime Number
def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 6. Odd/Even
def odd_even(n):
    """Checks if a number is odd or even."""
    return "Even" if n % 2 == 0 else "Odd"

# 7. Factorial
def factorial(n):
    """Calculates the factorial of a number."""
    if n < 0:
        return "Factorial not defined for negative numbers."
    return 1 if n == 0 else n * factorial(n - 1)

# 8. Linear Search
def linear_search(arr, x):
    """Searches for an element in an array using linear search."""
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# 9. Array Operations
def create_array():
    """Creates an array from user input."""
    arr = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        arr.append(element)
    return arr

# 10. Stack Operations
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty!"

    def is_empty(self):
        return len(self.items) == 0

# 11. Queue Operations
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        return "Queue is empty!"

    def is_empty(self):
        return len(self.items) == 0

# 12. Linked List Operations
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

# 13. Arithmetic Operations
def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers."""
    if y == 0:
        return "Division by zero error!"
    return x / y

def modulo(x, y):
    """Calculates the modulo of two numbers."""
    if y == 0:
        return "Modulo by zero error!"
    return x % y

# Example usage:
while True:
    print("\nSelect operation:")
    print("1. Serial Input")
    print("2. Fibonacci Sequence")
    print("3. GCD")
    print("4. LCM")
    print("5. Prime Number")
    print("6. Odd/Even")
    print("7. Factorial")
    print("8. Linear Search")
    print("9. Array Operations")
    print("10. Stack Operations")
    print("11. Queue Operations")
    print("12. Linked List Operations")
    print("13. Arithmetic Operations")
    print("14. Exit")

    choice = input("Enter choice (1-14): ")

    if choice == '1':
        numbers = get_serial_input()
        print("Entered numbers:", numbers)

    elif choice == '2':
        n = int(input("Enter the number of terms: "))
        fibonacci(n)

    elif choice == '3':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))

    elif choice == '4':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("LCM of", num1, "and", num2, "is:", lcm(num1, num2))

    elif choice == '5':
        num = int(input("Enter a number: "))
        print(num, "is a prime number." if is_prime(num) else f"{num} is not a prime number.")

    elif choice == '6':
        num = int(input("Enter a number: "))
        print(num, "is", odd_even(num))

    elif choice == '7':
        num = int(input("Enter a number: "))
        print("Factorial of", num, "is:", factorial(num))

    elif choice == '8':
        arr = create_array()
        x = int(input("Enter the element to search for: "))
        index = linear_search(arr, x)
        print(f"Element {x} found at index {index}" if index != -1 else f"Element {x} not found in the array")

    elif choice == '9':
        arr = create_array()
        print("Created array:", arr)

    elif choice == '10':
        stack = Stack()
        while True:
            print("\nStack Operations:")
            print("1. Push")
            print("2. Pop")
            print("3. Check if Empty")
            print("4. Back to Main Menu")

            stack_choice = input("Enter your choice (1-4): ")

            if stack_choice == '1':
                item = input("Enter the item to push: ")
                stack.push(item)
                print("Item pushed to the stack.")
            elif stack_choice == '2':
                print("Popped item:", stack.pop())
            elif stack_choice == '3':
                print("Stack is empty." if stack.is_empty() else "Stack is not empty.")
            elif stack_choice == '4':
                break
            else:
                print("Invalid Input")

    elif choice == '11':
        queue = Queue()
        while True:
            print("\nQueue Operations:")
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Check if Empty")
            print("4. Back to Main Menu")

            queue_choice = input("Enter your choice (1-4): ")

            if queue_choice == '1':
                item = input("Enter the item to enqueue: ")
                queue.enqueue(item)
                print("Item enqueued to the queue.")
            elif queue_choice == '2':
                print("Dequeued item:", queue.dequeue())
            elif queue_choice == '3':
                print("Queue is empty." if queue.is_empty() else "Queue is not empty.")
            elif queue_choice == '4':
                break
            else:
                print("Invalid Input")

    elif choice == '12':
        linked_list = LinkedList()
        while True:
            print("\nLinked List Operations:")
            print("1. Append")
            print("2. Display")
            print("3. Back to Main Menu")

            linked_list_choice = input("Enter your choice (1-3): ")

            if linked_list_choice == '1':
                data = input("Enter data to append: ")
                linked_list.append(data)
                print("Data appended to the linked list.")
            elif linked_list_choice == '2':
                current = linked_list.head
                print("Linked List: ", end="")
                while current:
                    print(current.data, end=" -> ")
                    current = current.next
                print("None")
            elif linked_list_choice == '3':
                break
            else:
                print("Invalid Input")

    elif choice == '13':
        while True:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print("\nSelect Arithmetic Operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Modulo")
            print("6. Back to Main Menu")

            arithmetic_choice = input("Enter your choice (1-6): ")

            if arithmetic_choice == '1':
                result = add(x, y)
                print(f"Result: {x} + {y} = {result}")
            elif arithmetic_choice == '2':
                result = subtract(x, y)
                print(f"Result: {x} - {y} = {result}")
            elif arithmetic_choice == '3':
                result = multiply(x, y)
                print(f"Result: {x} * {y} = {result}")
            elif arithmetic_choice == '4':
                result = divide(x, y)
                print(f"Result: {x} / {y} = {result}")
            elif arithmetic_choice == '5':
                result = modulo(x, y)
                print(f"Result: {x} % {y} = {result}")
            elif arithmetic_choice == '6':
                break
            else:
                print("Invalid Input")

    elif choice == '14':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid Input. Please select a valid option.")

