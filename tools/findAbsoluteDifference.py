def findAbsoluteDifference (a,b):
    suma = 0
    if a < b:
        suma = b - a
        return suma
    else:
        suma = a - b
        return suma
print(findAbsoluteDifference(3,6))