def findThrees():
    DATA = open("/Users/mario.jovanovic/Desktop/IB/Git_Hub_Repo/DP_CS_Code_MJovanovic/class25March/numbers.txt", "r")
    THREE = []
    for line in DATA: 
        ITEM = line.replace("\n", "")
        ITEM = int(ITEM)
        if ITEM > 99 and ITEM < 1000:
            F = ITEM // 100
            S = ITEM % 100 // 10
            T = ITEM % 10
            if F < S and S < T:
                THREE.append(ITEM)
    return THREE

print(findThrees())