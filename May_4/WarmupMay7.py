# 1. a. Surveys, interviews, observations to gain the insight how library is being used.
# 1. b. Test different feature to identify problems before it goes public.

# 2. 16 * 16 = 256
# 3. They hold data. They will transfer data from one computer to another. Header, packet, footer. 

# 4. 
'''
COUNTER = 0
SUMOFSTRINGLENGHTS = 0
C.resetNext()
loop while C.hasNext()
    TEMP = C.getNext()
    STRINGLENGHT = TEMP.getLenght()
    SUMOFSTRINGLENGHTS = SUMOFSTRINGLENGHTS + STRINGLENGHT
    COUNTER = COUNTER + 1
AVERAGE = SUMOFSTRINGLENGHTS / COUNTER
OUTPUT AVERAGE
'''

def sumOfFactorsOfN(n):
    factors = set()
    for i in range(1, int(n**1/2)+1):
        if n % i == 0:
            factors.add(i)
            factors.add(n//i)
    return sum(factors) - n

def amicableNumbers(n):
    amicableSet = set()
    for i in range(1, n+ 1):
        numA = sumOfFactorsOfN(i)
        numB = sumOfFactorsOfN(numA)
        if numB == i and numA!= numB:
            amicableSet.add(i)
            amicableSet.add(numB)
    return sum(amicableSet)

# print(amicableNumbers(1000))

def readFile(filename):
    f = open(filename, "r")
    myFile = f.read().replace("\"", "").split(",")
    myFile.sort()
    listOfLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(len(myFile)):
        suma = 0
        result = 0
        for j in range(len(myFile[i])):
            a = myFile[i][j]
            indexOfLetter = listOfLetters.index(a)
            suma = suma + indexOfLetter
        result = (suma) * i
        print(result)
# print(readFile("/Users/mario.jovanovic/Desktop/IB/Git_Hub_Repo/DP_CS_Code_MJovanovic/May_4/listA1.txt"))

def readFileA(filename):
    f = open(filename, "r")
    myFile = f.read().replace("\"", "").split(",")
    myFileA = sorted(myFile)
    return myFileA

def findTheValueOfWords(word):
    listOfLetters = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    suma = 0
    for i in range(len(word)):
        suma = suma + listOfLetters.index(word[i])
    return suma
# print(findTheValueOfWords("COLIN"))

def sumTheValuesOfWords():
    passTheFileHere = readFileA("/Users/mario.jovanovic/Desktop/IB/Git_Hub_Repo/DP_CS_Code_MJovanovic/May_4/listA1.txt")
    cummulativeSum = 0
    for i in range(len(passTheFileHere)):
        b = findTheValueOfWords(passTheFileHere[i])
        cummulativeSum = cummulativeSum + b
    return cummulativeSum
# The answer should be 324536!
# print(sumTheValuesOfWords())

def EulerP22():
    f = open("/Users/mario.jovanovic/Desktop/IB/Git_Hub_Repo/DP_CS_Code_MJovanovic/May_4/listA1.txt", "r")

    names = f.read()
    names = names.reaplace('"', "")
    names = names.split(",")

    sum = 0
    for i in range(len(names)):
        temp = 0
        for j in range(len(names[i])):
            temp += ord(names[i][j])-64
        temp *=(i+1)
        sum += temp
    return sum



def fibonacciDigit1000():
    fibonacci = [1]
    i = 1
    index = 0
    while len(str(i)) < 1000:
        fibonacci.append(int(i))
        i = i + fibonacci[index]
        index += 1
    return index + 2        

# print(fibonacciDigit1000())

def fibonacciDigit1000B():
    j = 1
    i = 1
    index = 1
    while len(str(i)) < 1000:
        temp = i
        i = i + j
        j = temp
        index = index + 1
    return index + 1        

# print(fibonacciDigit1000B())