
import random

secret_number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

while guess != secret_number:

    if guess > secret_number:
        print("Too high")

    elif guess < secret_number:
        print("Too low")

    guess = int(input("Try again: "))

print("Congratulations! You guessed correctly.")