def findModSum1(data):
    suma = 0
    for i in range(0, len(data), 1):
        if data[i] % 3 == 0:
            suma = suma + data[i]
    return suma
print(findModSum1([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))

print("Result should be 45!")