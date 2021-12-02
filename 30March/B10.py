def calcBMI(height, weight):
    heightsqrd = height ** (2)
    bmi = weight / heightsqrd
    return int(bmi)

def weightCategory(bmi):
    if bmi < 18.5:
        return bmi, "Underweight"
    if 18.5 <= bmi < 25.0:
        return bmi, "Normal Weight"
    if 25.0 <= bmi < 30.0:
        return bmi, "Overweight"
    return bmi, "Obese"

def askHeightWeight():
    print("Please Enter Your Height!!! (in metres)")
    h = float(input())
    print("Please Enter Your Weight!!! (in kilograms)")
    w = float(input())
    a = calcBMI(h, w)
    b = weightCategory(a)
    return b

print(askHeightWeight())