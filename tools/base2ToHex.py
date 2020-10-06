# Abstraction - Hiding the process of something

#To start class please review this algorithm for understanding. 
#We will be talking through it. 

def base2ToHex(s):

	#creates a constant list called HEX which holds all the hexademical characters
	#List: Lists are a data structure that are a reference type. 
	HEX = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
	
	#creates a primative variable called result which gets initalized to an empty String
	result = ""

	#This line adds 0's to the string so the lenght is divisible by 4. 
	#Python Specific: 3 * "hi" --> "hihihi"
	

	s =  (4-len(s)%4) * "0" + s #adds 0 to front of string to make len multiple of 4
	#Conversion Concept:
	#
	#	When converting from base2 to hex we break up the base 2 value into groups of 4
	#	starting from smallest digit (right
	#
	#   1111 0101
	#    F.    5
	#   0011 0101
	#     3   5
	#   0   4
	#   11110101
	#Looping the integers from 0 to the len(s) - 1 by 4 
	for i in range(0, len(s),4):

		#Pull out 4 characters from s going from index i to i + 4
		#Concept here: With substring the second value - first value = result lenght
		v = s[i: i + 4]
		#Converts the four digits to base 10
		#If v = 0110
		# index = 0 * 8 + 1 * 4 + 1 * 2 + 0 * 1 = 6
		index = int(v[0])*8 + int(v[1])*4 + int(v[2])*2 + int(v[3])*1
		#Self referencing Assignment Statement: 
		#Adding the hex value found in the list corrispoding to v
		result = result + HEX[index]

	
	return result


#TESTING:
BIN = [ "0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]

#print(base2ToHex("0010"))
#Simple Test Case
for i in range (0, len(BIN),1):
	print(base2ToHex(BIN[i]))

print(base2ToHex("1011110101"))
print(base2ToHex("101101011")) # 1 6 B
