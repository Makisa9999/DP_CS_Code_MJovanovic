
product_List = ["Mints", "Apple", "Banana", "Jelly", "Choco", "Strawberry", "Chicken", "Icecream", "Printer", "Sofa", "Chair", "Table"]
product_price = [1,1,2,2,3,1,4,5,51,5,1,2]

a = input("Enter the product you want: ")
    
for i in range(0,len(product_List),1):

    if a == product_List[i]:
        print(product_List[i])
        print(product_price[i])

if a not in product_List:
    print("Invalid Name") 