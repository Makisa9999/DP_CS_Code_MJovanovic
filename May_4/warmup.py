# Given a collection C that contains a string with the following format "<number>-<number>".  
# For example, valid elements include "45-99" and "101-23". The left sum is the sum of all the values
# to the left of the dash and the right sum is the sum of all the elements to the right of the dash. 
# For example if the collection C = ["99-4","101-32","65-1"] the left sum would be 99 + 101 + 65 
# and the right sum would be 4 + 32 + 1.  
'''

LEFTSUM = 0
RIGHTSUM = 0
C.resetNext()
loop while C.hasNext():
    TEMP = C.getNext()
    TEMP = TEMP.splitOn("-")
    LEFTSUM = LEFTSUM + TEMP[0]
    RIGHTSUM = RIGHTSUM + TEMP[1]
OUTPUT LEFTSUM, RIGHTSUM

'''
def warmupMay10th(collection):
    leftSum = 0
    rightSum = 0
    for i in range(len(collection)):
        temp = collection[i].split("-")
        leftSum = leftSum + int(temp[0])
        rightSum = rightSum + int(temp[1])
    return leftSum, rightSum

collection = ["23-1", "33-12"]
# print(warmupMay10th(collection))
