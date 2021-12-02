Arrays = [[0] * 401] * 200
inputs = ["0"]
while inputs[-1][0] != "q":
  temp = input()
  inputs.append(temp)

rows = 0
columns = 201
Arrays[rows][columns] = 1
for i in range(1,len(inputs),1):
  temporary = inputs[i].split(" ")
  if temporary[0] == "d":
    numberOfUnits = int(temporary[1])
    for i in range(numberOfUnits):
      rows = rows + 1
      if Arrays[rows][columns] == 1: 
        print(rows * (-1), columns - 201, "DANGER")
      else:
        Arrays[rows][columns] = 1
        print(rows * (-1), columns - 201, "SAFE")

        
  elif temporary[0] == "u":
    numberOfUnits = int(temporary[1])
    for i in range(numberOfUnits):
      rows= rows-1
      if Arrays[rows][columns] == 1:
        print(rows * (-1),columns - 201,"DANGER")
      else:
        Arrays[rows][columns] = 1
        print(rows * (-1),columns - 201,"SAFE")
        
  
  elif temporary[0] == "l":
    numberOfUnits = int(temporary[1])
    
    for i in range(numberOfUnits):
      columns = columns - 1
      if Arrays[rows][columns] == 1: 
        print(rows * (-1), columns - 201, "DANGER")
      else:
        Arrays[rows][columns] = 1
        print(rows * (-1), columns - 201, "SAFE")
  
  elif temporary[0] == "r":
    numberOfUnits = int(temporary[1])
    for i in range(numberOfUnits):
      columns = columns + 1
      if Arrays[rows][columns] == 1: 
        print(rows * (-1), columns - 201, "DANGER")
      else:
        Arrays[rows][columns] = 1
        print(rows * (-1), columns - 201, "SAFE")
  

# When d subtract from rows
# when l subtract from columns
# when u add to rows
# when r add to columns
# When q end


