from re import I


i = 1
total = 0
while i < 1001:
    total += i
    i += 1
print("The total is:", total)

total = 0
for j in range(1001):
    total += j
print("The total is:", total)