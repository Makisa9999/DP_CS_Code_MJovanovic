def findReversed (a):
    a = abs(a)
    astr = str(a)
    reverse = ""
    for i in range(len(astr) - 1, -1, -1):
        reverse = str(reverse) + astr[i]
        reverse = int(reverse)
    return reverse
print(findReversed(19))
print(findReversed(2283))
print(findReversed(-12))