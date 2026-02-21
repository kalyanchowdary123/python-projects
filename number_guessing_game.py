import random

print("Number Guessing Game")
print("Guess a number between 1 and 100")

secretnumber = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess "))
    attempts += 1

    if guess < secretnumber:
        print("Too low")
    elif guess > secretnumber:
        print("Too high")
    else:
        print("Correct You guessed ", attempts, "attempts")
        break