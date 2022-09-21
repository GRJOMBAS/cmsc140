num = int(input("Please enter a number to start from: "))
count = int(input("Please enter how much to count down by: ")) * -1
for num in range(num, -1, count):
    print(num)

# Code using a while loop instead
"""
num = int(input("Please enter a number to start from: "))
count = int(input("Please enter how much to count down by: ")) * -1
while num > -1:
    print(num)
    num += count
"""