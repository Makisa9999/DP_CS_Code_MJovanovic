lst = [1,2,3]
# result = []
# ctr = 0
# while (ctr < len(lst)):
#     result.insert(ctr, lst[ctr])
#     result.insert(ctr, lst(ctr))
#     ctr = ctr + 1
# print(result)

resultB = lst + lst[::-1]
print(resultB)