import random

num = int(random.random()*100)
print("The randomly generated number is:", num)
chain = 0
while num != 1:
    if num % 2 == 0:
        num = num // 2
        chain += 1
    else:
        num = (num*3) + 1
        chain += 1
print("Length of Chain:", chain)