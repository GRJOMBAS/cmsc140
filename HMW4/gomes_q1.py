a = [0, 1, 2, 3, 4, 5, 6, 7, 7, 9, 10, 11, 12, 13, 14, 16, 15, 17, 18, 18]
b = list(range(20))
c = []

def listdiff(a, b):
    for i in range(len(b)):
        if (b[i] != a[i]):
            c.append(b[i])
    return c

print(listdiff(a, b))