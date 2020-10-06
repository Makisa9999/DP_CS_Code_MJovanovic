def findModSum3(values,a,b):
    suma = 0
    for i in range(0, len(values), 1):
        if values[i] % a == 0 and values[i] % b == 0:
            suma = suma + values[i]
    return suma
print(findModSum3([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],2,5))

print("Result should be: 10!")