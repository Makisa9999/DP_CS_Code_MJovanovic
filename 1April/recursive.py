def binarySearch(A, left, right, x):
    if left > right:
        return -1
    mid = (left + right) // 2
    if x == A[mid]:
        return mid
    elif x < A[mid]:
        return binarySearch(A, left, mid - 1, x)
    else:
        return binarySearch(A, mid + 1, right, x)