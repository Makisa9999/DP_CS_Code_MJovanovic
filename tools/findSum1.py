def findSum1 (n):
    suma = 0
    for i in range(0, n+1, 1):
        suma = suma + i
    return suma
print(findSum1(5))