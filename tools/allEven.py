def allEven(n):
    
    even = True

    while (n > 0) and (even == True):
        if (n % 10) % 2 == 1 :
            even = False
        n = n // 10
        print(n)
    return even
print(allEven(345))
print(allEven(236))