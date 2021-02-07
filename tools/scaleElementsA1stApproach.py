def scaleElementsA(a, b):
	b[0] = b[0] * a
	b[1] = b[1] * a
	b[2] = b[2] * a
	b[3] = b[3] * a
	return b
print(scaleElementsA(2, [1,2,3,4]))
