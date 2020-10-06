def reverseWordB(a):

    reverse = ""
    reverse1 = ""
    for i in range(0, len(a), 1):
        reverse = a[i]
        for i in range(len(reverse)-1, -1, -1):
            reverse1 = reverse1 + reverse[i]
    return reverse1

print(reverseWordB(["cat","dog"]))