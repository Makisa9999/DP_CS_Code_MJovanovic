def toMeters (a, b):
    if b == "mm":
        a = int(a) / 1000
        return a
    elif b == "cm":
        a = int(a) / 100
        return a
    elif b == "dm":
        a = int(a) / 10
        return a
    else:
        return a
print(toMeters("12", "dm"))
print(toMeters("123", "cm"))
print(toMeters("1232", "mm"))