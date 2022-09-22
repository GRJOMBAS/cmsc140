num = int(input("Enter a number: "))
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