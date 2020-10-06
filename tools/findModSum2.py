def findModSum2(data,a,b):
    suma = 0
    for i in range(0, len(data), 1):
        if data[i] > a and data[i] < b:
            suma = suma + data[i]
    return suma
print(findModSum2([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],7,14))

print("Answer should be 63")