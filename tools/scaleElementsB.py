def scaleElementsB(a,b):
	c = []#creates empty list

	#.append adds a new element to the list
	for i in range(0, len(b),1):
		c.append(b[i]*a)

	return c

print("Start test code scale elements b")
l = [1,2,3,4]
print(l)
result = scaleElementsB(2,l)
print(result)