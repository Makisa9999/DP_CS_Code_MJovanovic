def isPrime(n):

    if n > 1:  
        for i in range(2,n):  
            if (n % i) == 0:  
                return False
 
        return True
    else:  
        return False

def isSemiPrime(n):
  for i in range(2, n, 1):
     if n % i == 0:
        d2 = n // i
        if isPrime(i) and isPrime(d2):
          return True
  return False

print(isSemiPrime(4))
print(isSemiPrime(15))
print(isSemiPrime(19))
print(isSemiPrime(21))
print(isSemiPrime(22))