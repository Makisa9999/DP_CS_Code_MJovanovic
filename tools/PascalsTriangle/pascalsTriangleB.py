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
    return pascal[-1]

print(pascalsTriangle())