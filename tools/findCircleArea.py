def findCircleArea (a):
    if a < 0:
        return -1
    elif a >= 0:
        pi = 3.14159
        asqrd = a ** 2
        total = 0
        total = asqrd * pi
        return round(total,3)

print(findCircleArea(-12))
print(findCircleArea(3))