import math

def sineLawAngle(a, A, b):
    # side a / sin (A) = side b / sin (B) = side c / sin (C)
    pairOne = a / math.sin(math.radians(A))
    bresult = b / pairOne
    result = math.degrees(math.asin(bresult))
    return result
# print(sineLawAngle(5.1, 100, 3.6))

def sineLawAngleRadian(a, A, b):
    # side a / sin (A) = side b / sin (B) = side c / sin (C)
    pairOne = a / math.sin(A)
    bresult = b / pairOne
    result = math.asin(bresult)
    return result
# print(sineLawAngle(5.1, 1.745329252, 3.6))

def sineLawSide(a, A, B):
    # side a / sin (A) = side b / sin (B) = side c / sin (C)
    pairOne = a / math.sin(math.radians(A))
    result = pairOne * math.sin(math.radians(B))
    return result
# print(sineLawSide(5.1, 100, 44))

def sineLawSideRadian(a, A, B):
    # side a / sin (A) = side b / sin (B) = side c / sin (C)
    pairOne = a / math.sin(A)
    print(pairOne)
    result = pairOne * math.sin(B)
    return result
# print(sineLawSide(5.1, 1.745329252, 0.7679448709))

print("Do you want in degrees or in radians? Enter 1 if you want degrees. Enter 2 if you want radians")
choice = input()
def mainFunction(c):
    if c == "1":
        print("Do you want to find the side or the angle? Input 1 for side. Input 2 for angle.")
        sideOrAngle = input()
        if sideOrAngle == "1":
            # side
            print("Please input side 'a'!")
            sideA = float(input())
            print("Please input angle opposite of side 'a'! This will be your angle A. In degrees!")
            angleA = float(input())
            print("Please input angle opposite of the side you want to find. In degrees!")
            angleOppResult = float(input())
            result = sineLawSide(sideA, angleA, angleOppResult)
            return result
        elif sideOrAngle == "2":
            # angle
            print("Please input side 'a'!")
            sideA = float(input())
            print("Please input angle opposite of side 'a'! This will be your angle A. In degrees!")
            angleA = float(input())
            print("Please input side opposite the angle you are trying to find! In degrees!")
            sideOppResult = float(input())
            result = sineLawAngle(sideA, angleA, sideOppResult)
            return result
        else: 
            return "Invalid Input! Please try again!"
    elif c == "2":
        print("Do you want to find the side or the angle? Input 1 for side. Input 2 for angle.")
        sideOrAngle = input()
        if sideOrAngle == "1":
            # side
            print("Please input side 'a'!")
            sideA = float(input())
            print("Please input angle opposite of side 'a'! This will be your angle A. In radians!")
            angleA = float(input())
            print("Please input angle opposite of the side you want to find. In radians!")
            angleOppResult = float(input())
            result = sineLawSideRadian(sideA, angleA, angleOppResult)
            return result
        elif sideOrAngle == "2":
            # angle
            print("Please input side 'a'!")
            sideA = float(input())
            print("Please input angle opposite of side 'a'! This will be your angle A. In radians!")
            angleA = float(input())
            print("Please input side opposite the angle you are trying to find! In radians!")
            sideOppResult = float(input())
            result = sineLawAngle(sideA, angleA, sideOppResult)
            return result
        else: 
            return "Invalid Input! Please try again!"
    else:
        return "Invalid Input! Please try again!"
print(mainFunction(choice))