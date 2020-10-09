import math
def findHyp (a, b):
    c = 0
    a2 = a ** 2
    b2 = b ** 2
    suma = a2 + b2
    c = math.sqrt(suma)
    return c
print(findHyp(3,4))