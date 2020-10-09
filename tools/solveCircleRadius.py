import math
def solveCircleRadius (a):
    pi = 3.14159
    if a < 0:
        return -1
    elif a >= 0:
        withoutpi = a / pi
        total = math.sqrt(withoutpi)
        return round(total,3)
print(solveCircleRadius(28.27431))
print(solveCircleRadius(-5))