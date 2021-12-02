import math
gravitationalConstant = 9.81
inputString = input("Enter values!")
inputString = inputString.split(" ")
angle = int(inputString[0])
power = int(inputString[1])
sinOfAngle = math.sin(math.radians(angle))
verticalSpeed = power * sinOfAngle
t = verticalSpeed / gravitationalConstant
t = 2 * t
cosOfAngle = math.cos(math.radians(angle))
horizontalSpeed = power * cosOfAngle
distanceTraveled = horizontalSpeed * t
distanceTraveled = round(distanceTraveled)
print(distanceTraveled)