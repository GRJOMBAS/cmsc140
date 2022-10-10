""" print("In class Exercise 1")

practiceDict = {
    5 : 20,
    2 : "Hello",
    "Hello" : 2
}

for key, value in practiceDict.items():
    print("Key is:", key, " Value is:", value) """

print("In class Exercise 2")

fridge = {
    "eggs" : 12,
    "milk" : 1,
    "cheese" : 2,
    "bread" : 3,
    "pizza" : 0.5
}

shopping_needs = ["eggs", "fruit", "milk", "juice"]

for i in shopping_needs:
    print(i)
    if i in fridge:
        print("You already have", fridge[i], i)  #fridge[i] to call value for key i
    else:
        print(i, "not in fridge")