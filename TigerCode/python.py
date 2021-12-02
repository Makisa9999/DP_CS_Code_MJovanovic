f = open("/Users/mario.jovanovic/Desktop/IB/Git_Hub_Repo/DP_CS_Code_MJovanovic/TigerCode/tiger.txt","r")

myfile = f.read()
myfile1 = myfile.split("\n")
lst = []
for i in range(len(myfile1)):
    if int(myfile1[i]) < 0 and int(myfile1[i]) > -12:
        lst.append(myfile1[i])

print(lst)
print(len(lst))