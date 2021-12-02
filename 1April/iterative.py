def binarySearch(A, x): 
    c = sorted(A)
    left = 0
    right = len(c) - 1
    while left <= right:
        # middle = int((left + right) / 2)
        middle = (left + right) // 2
        if x == c[middle]:
            return middle
        elif x < c[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1

c = [2,4,621,12,321,5,12,12,1,12,1,23,5,7565,56,5,5,6,656,565,6]
print(binarySearch(c, 321))
print(c)