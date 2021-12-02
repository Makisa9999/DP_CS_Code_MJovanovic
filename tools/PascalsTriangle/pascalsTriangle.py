# I want to make a program that will ask for the degree and then it will 
# calculate pascals triangle for that degree

# [1,1] --> 1 row
# [1,2,1] --> 2 row
# [1,3,3,1] --> 3 row
# [1,4,6,4,1] --> 4 row
# [1,5,10,10,5,1] --> 5 row
def pascalsTriangle():
    degree = int(input())
    pascal = []
    for i in range(degree + 1):
        pascal.append([0] * (i + 1))
    for i in range(len(pascal)):
        pascal[i][0] = 1
        pascal[i][-1] = 1
        for j in range(len(pascal[i])):
            if pascal[i][j] == 0:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
            else:
                pass
    for i in range(len(pascal)):
        for j in range(len(pascal[i])):
            print(pascal[i][j], end=' ')
        print()

    return "DONE!"

print(pascalsTriangle())
# degree = int(input())
# pascal = []
# for i in range(degree + 1):
#     pascal.append([0] * (i + 1))
# for i in range(len(pascal)):
#     pascal[i][0] = 1
#     pascal[i][-1] = 1
#     for j in range(len(pascal[i])):
#         if pascal[i][j] == 0:
#             pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
#         else:
#             pass

# print(pascal)

# # for i in range(len(pascal)):
# #     for j in range(len(pascal[i])):
# #         print(pascal[i][j], end=' ')
# #     print()