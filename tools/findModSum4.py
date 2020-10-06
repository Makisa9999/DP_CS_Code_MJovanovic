
def findModSum4(d):

    suma = 0
    a = ""
    b = 0

    for i in range(0, len(d), 1):
        #variable should always be on the left hand side.
        a = str(d[i])
        #when you want to replace t
        a = a.replace(".", "")
        for i in range(0, len(a), 1):
            b = int(a[i])
            suma = suma + b
    return suma

print(findModSum4([1.2,3.14,7.89]))

print("Should get 35!")

