

def longestCollatz():
    start = int(input("Enter a start: "))
    stop = int(input("Enter a stop: ")) + 1
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

print(longestCollatz)