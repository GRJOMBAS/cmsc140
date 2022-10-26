import random


def randomNumberGuesser():
    randomNumber = int(random.random() * 100) + 1
    tries = int(input(("How many gusses?\n"))) 
    print("Welcome to the random number guesser.")
    #print(randomNumber) # uncomment to make it easier to check for correct guess
    guess = int(input("Please input a number between 1 and 100 ("+ str(tries)+ " guesses left): "))
    

    if guess == randomNumber:
        print("Congrats! you got it right on your first try!")
    
    else:    
        while (guess != randomNumber):
            tries -= 1
            if (tries == 0):
                print("Sorry, you lost. The correct number was", randomNumber)
                break
            if (guess > randomNumber):
                guess = int(input(str(guess) + " is too high! Try Again ("+ str(tries)+ " guesses left): "))
            elif (guess < randomNumber):
                guess = int(input(str(guess) + " is too low! Try Again ("+ str(tries)+" guesses left): "))
                
            elif (guess == randomNumber):
                print("Congrats!", guess, "was correct! You got it right!")
                break
            
            

randomNumberGuesser()

