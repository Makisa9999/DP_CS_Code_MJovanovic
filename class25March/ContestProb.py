def findroot(s):
    start = 0
    end = 1
    for i in range(0, len(s), 1):
        result = len(s) % len(s[start:end]) == 0 and s.count(s[start:end]) == len(s)/len(s[start:end])

        if result == True:
            print(s[start:end])
            return
        end = end + 1

    return s

file = open("/Users/mario.jovanovic/Desktop/IB/Git_Hub_Repo/DP_CS_Code_MJovanovic/class25March/numbers.txt", "r")

data = file.read().split("\n")

for j in range(0, len(data), 1):
    findroot(data[j])