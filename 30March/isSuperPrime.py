def isSuperPrime(n):
    for i in range(2, n // 2 + 1, 1):
        if n % i == 0:
            return "not super prime, not even prime"
        
    primes = []
    for j in range(2, n + 1, 1):
        check = 0
        for i in range(2, j // 2 + 1, 1):
            if j % i == 0:
                check = check + 1
        if check == 0:
            primes.append(j)
        
    nIndex = primes.index(n) + 1

    if nIndex in primes:
        return True
    
    return False

print(isSuperPrime(11))