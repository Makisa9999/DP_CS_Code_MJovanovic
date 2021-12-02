print("Do you want to find the angle or the side with cosine rule? Input '1' if you want to find the angle. Input '2' if you want to find the side.")
whichOne = input()
def mainFunction(n):
    if n == '1':
        # Ask for input for all 3 sides.
        print("Input side 1!")
        side1 = input()
        print("Input side 2!")
        side2 = input()
        print("Input side 3!")
        side3 = input()
        # Pass all three sides in the function for calculation for the angle!
        # Store the value that you get from the function in a variable.
        # Example resultAngle = calculationOfAngle(side1, side2, side3)
        # At the end return resultAngle
    elif n == '2':
        # Ask for input for 2 sides and angle.
        print("Input side 1!")
        side1 = input()
        print("Input side 2!")
        side2 = input()
        print("Input angle (in degrees)!")
        angle = input()
        # Pass everything in the function for the calculation of the third side!
        # Store the value that you get from the function in a variable.
        # Example resultSide = calculationOfSide(side1, side2, angle)
        # At the end return resultSide
    else: 
        return "Invalid Input! Please try again!"
print(mainFunction(whichOne)) 