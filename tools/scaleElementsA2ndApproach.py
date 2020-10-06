def scaleElementsA(a,b):
	print("Scale Elements A")
	#I need to loop through every element and miltiply it by a
	for i in range(0, len(b), 1):
		b[i] = a * b[i]
print("START TEST CODE SCALE ELEMENTS A")
l = [1,2,3,4]
print(l)
scaleElementsA(2,l)
print(l)