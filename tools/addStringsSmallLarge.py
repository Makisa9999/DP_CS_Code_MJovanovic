def addStringsSmallLarge(a,b):
    anumb = len(a)
    bnumb = len(b)
    stringc = ""
    if anumb > bnumb:
        stringc = a + b
    elif anumb < bnumb:
        stringc = b + a
    return stringc
print(addStringsSmallLarge("Notebook", "Calculator"))