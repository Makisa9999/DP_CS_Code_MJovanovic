def findingTheSameElements(lst):
    same = set()
    for i in range(len(lst)):
        for j in range(i, len(lst), 1):
            if lst[i] == lst[j]:
                same.add(lst[i])
            else:
                pass
    return same               

lst = [1,2,2,3,4,6,5,4,32,2,2,21,1,2,3,45,7,7]
print(findingTheSameElements(lst))