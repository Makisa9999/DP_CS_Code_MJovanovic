def primes_sieve2(limit):
    
    a = [True] * limit                          # Initialize the primality list

    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
    
        if isprime:
    
            yield i
    
            for n in range(i*i, limit, i):     # Mark factors non-prime
    
                a[n] = False


# print(primes_sieve2(15))

def sieveOfEratosthenes(n):
    primeList = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primeList[p] == True):
            for i in range(p * p, n + 1, p):
                primeList[i] = False
        p = p + 1
    for p in range(2, n + 1):
        if primeList[p] == True:
            print(p)
    return "Done"

print(sieveOfEratosthenes(100))