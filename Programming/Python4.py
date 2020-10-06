name = "Mario Jovanovic"
height = 1.9
weight = 92

bmi = weight / (height ** 2)
print("bmi:")
print(bmi)
if bmi < 25:
	print(name)
	print("is not overweight!")
else: 
	print(name)
	print("is overweight!")