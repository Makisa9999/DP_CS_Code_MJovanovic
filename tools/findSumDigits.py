def findSumDigits (a):
    if a > 1000:
        print("Invalid Input:")
        return a
    elif a < 0:
        print("Invalid Input:")
        return a
    else: 
        astr = str(a)
        suma = 0

        for i in range(0, len(astr), 1):
            suma = suma + int(astr[i])
            return suma

print(findSumDigits(123))
print(findSumDigits(-122))
print(findSumDigits(1002))
