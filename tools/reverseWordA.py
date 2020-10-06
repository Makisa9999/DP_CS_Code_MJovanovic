def reverseWordA(a):
    reverse = ""
    for i in range(len(a) - 1, -1, -1):
        reverse = reverse + a[i]
    return reverse

print(reverseWordA("cat"))
