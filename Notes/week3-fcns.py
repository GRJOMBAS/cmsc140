""" #fucntions

def main():    # def (function name)():
    print("this is a function")

main()

def excitedPrint(myString):
    print(myString + "!!!!!!")
excitedPrint("Hello")
excitedPrint("This is a fucntion")

def numSquare(num):
    return num*num

print(numSquare(3)) """
 
""" print("This is Exercise 1")

def exponent(num, exp):
    return num ** exp
ex1 = exponent(7, 3)
ex2 = exponent(4, 2)
ex3 = exponent(25, 0.5)
print(ex1)
print(ex2)
print(ex3) """

""" print("Exercise 2a")
num = int(input("Enter a number: "))

def collatz(num):
    chain = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
            print("Div by 2: ", num)
            chain += 1
        else:
            num = (num*3) + 1
            print("Times 3 Plus 1: ", num)
            chain += 1
    print("Length of Chain: ", chain)

collatz(num) """

print("Exercise 2b")
startingNum = int(input("Enter a start: "))
endingNum = int(input("Enter a stop: ")) + 1

def longestCollatz(start, stop):
    largestChain = 0
    for num in range(start, stop):
        chain = 0
        sequenceNum = num
        while num != 1:
            if num % 2 == 0:
                num = num // 2
                chain += 1
            else:
                num = (num*3) + 1
                chain += 1
        if chain > largestChain:
            largestChain = chain
            largestNum = sequenceNum
    return largestNum

print(longestCollatz(startingNum, endingNum))