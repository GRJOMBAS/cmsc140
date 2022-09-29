def fsum(start, stop):
        total = 0
        for num in range(start, stop + 1):
            total += num;
        return total
    #print(sum([i for i in range(start, stop + 1)]))    # one liner: 

def countdown(startingNum, count):
        for startingNum in range (startingNum, -1, count):
            print(startingNum)
    #print("\n".join([str(i) for i in range(startingNum, -1, count)]))  # one liner
        

def functionChooser():
    print("Welcome to the function chooser. Please choose a function.")
    print("1 = Cumulative Sum")
    print("2 = Countdown")
    choice = int(input("Your choice: "))
    if choice == 1:
        num1 = int(input("Enter an integer for a starting point: "))
        num2 = int(input("Enter an integer for an ending point: "))
        print(fsum(num1, num2))
    elif choice == 2:
        num1 = int(input("Enter a number is the number to start from: "))
        num2 = int(input("Enter how much to count down by: ")) * -1
        countdown(num1, num2)

functionChooser()





