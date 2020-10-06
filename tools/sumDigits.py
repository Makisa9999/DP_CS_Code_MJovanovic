def sumDigits(a):

	total = 0
	#Casting is the process of changing type.
	a = str(a)

	#Fundamental skill: Looping through string

	#Count, Check, Change
	for i in range(0, len(a),1):
		total = total + int(a[i])
	return total
print(sumDigits(1234))