"""
# while loops
classcode = "CMSC 140"
if classcode == "CMSC 140":
    print("Welcome to Class!")

while classcode == "CMSC 140":
    print("Welcome to Class!")
    classcode = "CMSC 150"
print("The while loop is over")
print(classcode)

timesThrough = 0
while timesThrough < 5:
    timesThrough = timesThrough + 1
    print("This has executed", timesThrough, "times")
print("times_through:", timesThrough)


print("In class exercise:")
num = int(input("Please input a number: "))
counter = 0
print("Initial number:", num)
while num > 1:
    num = num // 2 # double division gives integer as output
    counter += 1
    print("Num:", num, "   counter:", counter)

# for loops
timesThrough = 0
print("For Loop")
for timesThroughFor in range(5):
    timesThroughFor += 1
    print("This has executed", timesThroughFor, "times")
print("times_through:", timesThroughFor)

i = 1
for i in range (11):
    print("For:", i, "squared is", i**2)

i = 1
while i < 11:
    print("While:", i, "squared is", i**2)
    i += 1
"""
print("In class exercise 2.0:")
for i in range (1001):
    if i % 2 == 0:
        print(i)

print("In class exercise 2.1:")
for j in range (0, 1001, 2):
    print(j)

print("In class exercise 2.2:")
k = 0
while k < 1001:
    print(k)
    k += 2




