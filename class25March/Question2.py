def isPrime(n):
    if n > 1:  
        for i in range(2,n):  
            if (n % i) == 0:  
                return False 
        return True
    else:  
        return False

def sumPrime():
    n = int(input())
    suma = 0
    for i in range(0, n, 1):
        a = isPrime(i)
        if a == True:
            suma = suma + i
    return suma

print(sumPrime())