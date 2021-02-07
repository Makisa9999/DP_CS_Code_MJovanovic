AppendingList = []

myfile = open("DP_CS_Code_MJovanovic/tools/NewFolder/listA1.txt", "r")
myfile2 = open("DP_CS_Code_MJovanovic/tools/NewFolder/listA2.txt", "r")

item = myfile.read().split("\n")
item2 = myfile2.read().split("\n")

for i in range (len(item)):
    for j in range(len(item2)):
        if item2[j] == item[i]:
            AppendingList.append(item2[j])

print(AppendingList)