import random

randomNumber = int(random.random() * 100)
print("Welcome to the random number guesser.")
print(randomNumber) # uncomment to make it easier to check for correct guess
guess = int(input("Please input a number between 1 and 100: "))
if guess == randomNumber:
    print("Congrats! you got it right on your first try!")
else:    
    while guess != randomNumber:
        if guess > randomNumber:
            guess = int(input(str(guess) + " is too high! Try Again: "))
        else:
            guess = int(input(str(guess) + " is too low! Try Again: "))
print("Congrats!", guess, "was correct! You got it right!")
