""" # Open a file
hello = open('hello.txt', 'a')

# Read and/or write
fileContents = hello.read()
fileContentsList = hello.readlines()
print(fileContents)
print(fileContentsList)



# Close the files
hello.write("\nGabriel Gomes")
hello.close()
 """
""" with open ('hello.txt', 'r') as f:
    info = [i.strip() for i  in f.readlines()]

for i in info:
    print(i) """

def printList(list):
    for i in list:
        print(i)

firstNames = []
lastNames = []
with open('hello.txt') as f:
    next(f)
    for line in f.readlines():
        x, y = line.split(" ")
        firstNames.append(x)
        lastNames.append(y)
printList(firstNames)
printList(lastNames)
