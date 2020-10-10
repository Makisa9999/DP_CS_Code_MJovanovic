def reverseNumber (a):
    astr = str(a)
    final0 = ""
    final = ""
    for i in range(len(astr) - 1, -1, -1):
        final0 = final0 + astr[i]
        final = int(final0)
    return final
print(reverseNumber(321))
print(reverseNumber(31212))
print(reverseNumber(118))
