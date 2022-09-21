
my_number = 7
my_string = "CMSC 140"
my_bool = True

# and
print(True and True)
print(True and False)
print(False and False)

#or
print("T or T", True or True)
print("T or F", True or False)
print("F or T", False or True)
print("F or F", False or False)

#not
print("not T", not True)
print("not F", not False)

print(True and not (True and False))

# Comparison Operators
    #equals and not equals

print("7 == 7", 7 == 7)
print("7 != 7", 7 != 7)
print("hello" == "hello") #True
print(True == False)
print(7 == "7")
print(1 + 2 == 3)
print("hi" + "hi" == "hihi")

print("Greater Than/Equals to")
#greater than/ geq
print(7 > 5)
print(4+1>5)
print(4+1 >= 5)
print("a" < "b")
print("cow" < "cat")
print(True > True)
print(True >= True)

#less than/ leq
print(7<5)
print(3 <= 2 + 2)

print(my_number, my_string, my_bool)


print("In-class Exercises")
print("cottage" < "cotton") #True
print(("Hello" != "hello") or 7 == 3) #True
print( 32 >= -467 and "CS140" == "CS 140") #false


#If Statements!
# if something is true
#       do something

if True:
    print("Hello")

if False:
    print("Secret message that will never run")

i = 0
if i == 0:
    print("i is 0")

i = 7
if i < 10:
    i = 10
    print(i)
    y = 25
    print(y)
    if 7 == 7:
        print("7 is 7")
    print (2 + 2)

print("i is", i)
print("i is " + str(i))

example = 10
if example < 10:
    print("Small number")
elif example == 10:
    print("It's 10")
else:
    print("Big number")

print("Name Exercise")
print("What is your name?")
myName = "Gabriel"
userName = input()

if userName > myName:
    print("Your name comes after mine in the alphabet")
elif userName < myName:
    print("Your name comes before mine in the alphabet")
elif userName == myName:
    print("We have the same name!")

print("Calculator Exercise")
print("Welcome to the Calculator")
print("Enter number 1: ")
num1 = input()
print("Enter number 2:")
num2 = input()
print("Enter operation [a, s, d, m]:")
operation = input()
if operation == "a":
    print(num1, "added with", num2, "is", num1 + num2)
elif operation == "s":
    print("subtracting", num1, "from", num2, "is", num1 - num2)
elif operation == "m":
    print(num1, "multiplied by", num2, "is", num1 * num2)
elif operation == "d":
    print(num1, "divided by", num2, "is", num1/num2)
else:
    print("That is not a valid operation")

