def findLargeSum (a,b,c):
    suma = 0
    if a < b < c:
        suma = b + c
        return suma
    elif b < a < c:
        suma = a + c
        return suma
    elif c < a < b:
        suma = a + b
        return suma
    elif a < c < b:
        suma = b + c
        return suma
    elif c < b < a:
        suma = a + b
        return suma
    else:
        suma = b + c
        return suma

print(findLargeSum(2,3,1))
print(findLargeSum(31,51,42))