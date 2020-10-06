def sumDigitsA(a):
	total = 0

	while (a > 0):
		total = total + a % 10 #acess the ones digit
		a = a // 10

	return total
print(sumDigitsA(57))
