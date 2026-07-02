import random
number = random.randint(1, 10)
while True:
    Guess = int(input("Guess a number between 1 and 10:"))
    if Guess == number:
        print("Congrats your Guessed number is absolutely correct.")
        break
    elif Guess < number:
        print("Too low!Try again.")
    else:
        print("Too High!Try again.")
