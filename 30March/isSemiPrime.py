def isPrime(n):
    if n > 1:  
        for i in range(2,n):  
            if (n % i) == 0:  
                return False
        return True
    else:  
        return False

def isSemiPrime(number):
    for i in range(2, number+1):
        if number % i == 0: 
            d2 = int(number / i)
            return isPrime(d2) and isPrime(i)
    return False

print(isSemiPrime(6))
print(isSemiPrime(9))
print(isSemiPrime(8))
print(isSemiPrime(1829))
print(isSemiPrime(1827))