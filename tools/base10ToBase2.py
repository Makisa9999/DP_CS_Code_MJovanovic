#See bottom for theory:

def base10toBase2(n):

	result = ""

	while (n > 0):

		result = str(n%2) + result
		n = n // 2
	

	return result

print(base10toBase2(45))

'''
Theory: To convert from Base 10 to any other base we 
divide by the new base (in this case 2) and use the remainder
and quotient to find the next step.  We stop when we reach 0
62 = 
62/2 = 31 R 0
31/2 = 15 R 1
15/2 = 7 R 1 
 7/2 = 3 R 1
 3/2 = 1 R 1 
 1/2 = 0 R 1
 DONE
 Read bottom up 
 62 = 111110
	Makes sesne since 62 is even and therefore the right
	most digit should be 0. 
 
45 = 101101
45/2 = 24 R 1
22/2 = 11 R 0
11/2 = 5  R 1
 5/2 = 2  R 1
 2/2 = 1  R 0
 1/2 = 0  R 1
 DONE
 Read bottom up - 45 = 101101
'''

#Question: How would I generalize this to base B


def base10toBaseB(n,b):

	result = ""

	while (n > 0):

		result = str(n%3) + result
		n = n // b
	

	return result

print(base10toBaseB(11,3))
