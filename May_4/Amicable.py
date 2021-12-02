# Write a function that takes an integer n and returns a list of all factors. 
def factors(n):
    a = []
    suma = 0
    for i in range(1, n, 1):
        if n % i == 0:
            a.append(i)
    for i in range(len(a)):
        suma = suma + a[i]
    return suma

# print(factors(25012))

def sumAmicableNum(n):
    suma = 0
    amicNum = []
    for i in range(n):
        a = factors(i)
        b = factors(a)
        if i == b and i != a and amicNum.index(i) == -1:
            amicNum[i].append(a)
    sumb = 0
    for i in range(len(amicNum)):
        sumb = sumb + amicNum[i]
    return sumb

print(sumAmicableNum(1000))

# ?????