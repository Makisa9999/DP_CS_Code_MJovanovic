lst = [1231,15421311,2312,3123,1231231,231231,23,1231,23,1,23,123,1,23,123,23]
a = lst[0]
for i in range(1, len(lst), 1):
    if lst[i] > a:
        a = lst[i]
    
print(a)
    