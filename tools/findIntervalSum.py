def findIntervalSum (a, b):
    if a < b:
        minimum = a
        maximum = b
        suma = 0
        for i in range(minimum, maximum + 1, 1):
            suma = suma + i
        return suma
    else:
        minimum = b
        maximum = a
        suma = 0
        for i in range(minimum, maximum + 1, 1):
            suma = suma + i
        return suma

print(findIntervalSum(12,15))