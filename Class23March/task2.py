def printNumbers(dictionary):
    d = list(dictionary.keys())
    total = 0
    for i in range(len(d)):
        if type(dictionary[d[i]]) != str:
            total = total + dictionary[d[i]]
    return total
d = {"key1":"value1", "key2":"value2", "key3":12, "key4": 23, "key5": 1}
print(printNumbers(d))

def printNumbers2(list):
    total = 0
    for i in range(len(a)):
        if type(a[i]) != str:
            total = total + a[i]
    return total
a = ["Mario", 21, "Mario2", "1", 12.123]
print(printNumbers2(a))

# Do the SL and HL questions, and make a dictionary function that shows your understanding of dictionaries
# Idea for dictionaries: 
# Make a function that will store what colors you want your car to be in.