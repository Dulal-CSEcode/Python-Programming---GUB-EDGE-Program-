import random
number = random.randint(1, 100)
attempts = 5
print("Guess the number between 1 and 100. You have 5 attempts.")
while attempts > 0:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("Congratulations! You guessed it right.")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")
    attempts -= 1
if attempts == 0:
    print(f"Sorry, you're out of attempts. The number was {number}.")