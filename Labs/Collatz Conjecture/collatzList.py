startingNum = int(input("Enter a start: "))
endNum = int(input("Enter a stop: ")) + 1
chainList = []
for num in range(startingNum, endNum):
    chain = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
            chain += 1
        else:
            num = (num*3) + 1
            chain += 1
    chainList.append(chain)
    largestChain = max(chainList)
    chainNum  = chainList.index(largestChain) + startingNum
print("Longest chain is from:", largestChain)
print("Length of chain:", chainNum)