def base2to10(str):
	n = 0
	total = 0

	for i in range(len(str) -1, -1, -1):
		total = total + int(str[i]) * 2**n
		n = n + 1
	return total

print(base2to10("011001"))