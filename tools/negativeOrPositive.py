def negativeOrPositive(a):
    for i in range(0, len(a), 1):
        if a[i] < 0:
            print("This is a negative number!")
        elif a[i] >= 0:
            print("This is a positive number!")

a = [-1,-2,-3,-4,-5,-6,0,1,2,3,4,5,6,7,8,9]
print(negativeOrPositive(a))