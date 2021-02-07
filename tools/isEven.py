def isEven(a):
    if a >= 0:
        if a % 2 == 0:
            return True
        return False
    else:
        return "Invalid Number!"
        
print(isEven(2))
print(isEven(3))
print(isEven(-3))