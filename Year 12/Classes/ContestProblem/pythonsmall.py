grid = []
t = [0,0,0,0,0,0,0,0,0,0,0] 

for i in range(0,10,1):
  grid.append(t.copy())

inputs = []
temp = 1
while temp != "q":
    temp = input()
    inputs.append(temp)

rows = 0
columns = 5
grid[rows][columns] = 1

for i in range(len(grid)):
    print(grid[i])

for i in range(1, len(inputs), 1):
    temporary = inputs[i].split(" ")
    if temporary[0] == "d":
        numberOfUnits = int(temporary[1])
        for i in range(numberOfUnits):
            rows += 1
            if grid[rows][columns] == 1:
                print("Danger!")
            else:
                grid[rows][columns] = 1
                for i in range(len(grid)):
                    print(grid[i])
                print("Safe!")
    if temporary[0] == "u":
        numberOfUnits = int(temporary[1])
        for i in range(numberOfUnits):
            rows -= 1
            if grid[rows][columns] == 1:
                print("Danger!")
            else:
                print("Safe!")
    if temporary[0] == "l":
        numberOfUnits = int(temporary[1])
        for i in range(numberOfUnits):
            columns -= 1
            if grid[rows][columns] == 1:
                print("Danger!")
            else:
                print("Safe!")
    if temporary[0] == "r":
        numberOfUnits = int(temporary[1])
        for i in range(numberOfUnits):
            columns += 1
            if grid[rows][columns] == 1:
                print("Danger!")
            else:
                print("Safe!")