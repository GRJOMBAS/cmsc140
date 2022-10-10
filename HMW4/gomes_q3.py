import random


def randomNumberGuesser():
    storage = []
    randomNumber = int(random.random() * 100) + 1
    tries = int(input(("How many gusses?\n"))) -1
    print("Welcome to the random number guesser.")
    #print(randomNumber) # uncomment to make it easier to check for correct guess
    guess = int(input("Please input a number between 1 and 100: "))
    storage.append(guess)

    if guess == randomNumber:
        print("Congrats! you got it right on your first try!")
        print("This was your guess average:", guess)
    
    else:    
        while (guess != randomNumber):
            
            if (tries == 0):
                print("Sorry, you lost. The correct number was", randomNumber)
                break
            if (guess > randomNumber):
                guess = int(input(str(guess) + " is too high! Try Again ("+ str(tries)+ " guesses left): "))
                storage.append(guess)
            if (guess < randomNumber):
                guess = int(input(str(guess) + " is too low! Try Again ("+ str(tries)+" guesses left): "))
                storage.append(guess)
            if (guess == randomNumber):
                print("Congrats!", guess, "was correct! You got it right!")
                
                break
            tries -= 1
    total = sum(storage)/len(storage)
    print("This was your guess average:", total)

randomNumberGuesser()