#New function called base10ToBase2 that takes parameter n
def base10toBase2(n):
    #We make a new variable called result and make it equal to an empty string
	result = ""
    #We make a loop that will be executed of n is greater than 0
	while (n > 0):
        #We take the result empty string and assign it a new value of n mod 2
		result = str(n%2) + result
        #We divide starting number so we can continue to write binary number
		n = n // 2
	
    #Just return this value to result
	return result
#Print out the function of a number 45
print(base10toBase2(45))

#Here we make new function called base2To10 and it needs a string element
def base2to10(str):
    #We make a variable n and set it to 0
	n = 0
    #We make a variable total and set it to 0
	total = 0
    #We make a for i in range loop that goes from the last character to the front of the str
	for i in range(len(str) -1, -1, -1):
        #Here we take a total and asign it the value of number that is on the position of i
        #and multiply it by 2 to the power of n
		total = total + int(str[i]) * 2**n
        #n will increase every time we pass through this loop
		n = n + 1
    #Just store the new value of total
	return total
#Print out the function of the number 011001
print(base2to10("011001"))



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

	#Just store the value of result
	return result


#TESTING:
#We made a list of numbers that will be tested
BIN = [ "0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]

#print(base2ToHex("0010"))
#Simple Test Case
#This will loop through the whole BIN list and print each number in HEX
for i in range (0, len(BIN),1):
	print(base2ToHex(BIN[i]))
#print the function of the number 1011110101
print(base2ToHex("1011110101"))
#print the function of the number 101101011
print(base2ToHex("101101011")) # 1 6 B



#This is a new function with a name hexToBase2_B that takes parameter s
def hexToBase2_B(s):
    #Here we make a new variable that is called result and set it up as an empty string
	result = ""
    #Here we made a list that contains Hex numbers and binary numbers
	DIC = { "0":"0000",
			"1":"0001",
			"2":"0010",
			"3":"0011",
			"4":"0100",
			"5":"0101",
			"6":"0110",
			"7":"0111",
			"8":"1000",
			"9":"1001",
			"A":"1010",
			"B":"1011",
			"C":"1100",
			"D":"1101",
			"E":"1110",
			"F":"1111"}

	#Here we make a for i in range loop that is going to go character by character 
	for i in range(0, len(s), 1):
        #This is going to convert the pairs of letters in DIC list to the binary code that
        #they represent
		result = result + DIC[s[i]]
    #stores result
	return result

#Testing our program
print(hexToBase2_B("0"))
print(hexToBase2_B("A12"))
print(hexToBase2_B("F"))


#Here we create a new function called sumDigits that takes parameter a
def sumDigits(a):
    #setting the total to 0
	total = 0
	#Casting is the process of changing type.
    #Here we are changing the type of a to a string
	a = str(a)

	#Fundamental skill: Looping through string

	#Count, Check, Change
    #Here we are making a loop that is going to go through every letter in a 
	for i in range(0, len(a),1):
        #Here we do the process of casting again,
        #and we add a as an integer to total 
		total = total + int(a[i])
    #return the total and store it
	return total
#Testing:
print(sumDigits(1234))


#We make a function that is called findModSum1 that takes parameter data
def findModSum1(data):
    #Here we create a new variable that is called suma and it is equal to zero
    suma = 0
    #Here we make a for i in range loop that is going to travel through every element in data
    for i in range(0, len(data), 1):
        #If the number in a list is divisible by 3 go in the loop
        if data[i] % 3 == 0:
            #add that number to suma
            suma = suma + data[i]
    #Store suma
    return suma
#Testing:
print(findModSum1([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
#Predicted result
print("Result should be 45!")


#Here we make a new function that will take parameters data, a, and b
def findModSum2(data,a,b):
    #Here we make a new variable called suma and set it to 0
    suma = 0
    #Here we make a loop that will go through every element in the list
    for i in range(0, len(data), 1):
        #Here we test if the element in data is bigger than a and if it is smaller than b 
        if data[i] > a and data[i] < b:
            #Here if the test is passed we add that number to suma 
            suma = suma + data[i]
    #Here we store suma
    return suma
#Testing:
print(findModSum2([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],7,14))
#This is printing what result should be
print("Answer should be 63")


#Here we make a function called findModSum3 that takes parameters values, a, and b
def findModSum3(values,a,b):
    #Here we make a variable called suma and set it to zero
    suma = 0
    #Here we make a loop that will go through every value in the list values
    for i in range(0, len(values), 1):
        #Here we test if element in values is divisible by a and by b
        if values[i] % a == 0 and values[i] % b == 0:
            #If the test passed then I am going to add that value to suma
            suma = suma + values[i]
    #Here we store the value suma
    return suma
#Testing:
print(findModSum3([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],2,5))
#Here we print out what the result should be
print("Result should be: 10!")



#Here we make a new function that is called findModSum4 that takes the parameter d
def findModSum4(d):
    #Here we make a new value suma and set it to 0
    suma = 0
    #Here we make a new value a and set it to empty string 
    a = ""
    #Here we make a new value b and set it to 0
    b = 0
    #Here we make a loop that is going to go through every element in d
    for i in range(0, len(d), 1):
        #Variable should always be on the left hand side.
        #Here we do the process of casting and change a to a string of "d" at "i"
        a = str(d[i])
        #When you want to replace t
        #Here we take every dot in a and replace it with an empty string
        a = a.replace(".", "")
        #Here we make a new loop that will go and separate every value of a into parts
        for i in range(0, len(a), 1):
            #Here we do the process of casting again and set to b every part of a as an integer
            b = int(a[i])
            #Here we add b to suma
            suma = suma + b
    #Store the value of suma
    return suma
#Here is the test case
print(findModSum4([1.2,3.14,7.89]))
#This is the expected result
print("Should get 35!")


#Here we make a new function call it reverseWordA and it takes parameters a
def reverseWordA(a):
    #Here we make a new variable called reverse and set it to empty string
    reverse = ""
    #Here we make a for loop that is going to start at the end of a string and go towards
    #the front of the string
    for i in range(len(a) - 1, -1, -1):
        #Here we store the value of a in i to the reverse variable
        reverse = reverse + a[i]
    #Store the reverse value
    return reverse
#Testing
print(reverseWordA("cat"))


#Here we make a new function called reverseWordB that takes parameter a which is a list
def reverseWordB(a):
    #Here we make a new variable and make it equal to empty string
    reverse = ""
    #Here we make a new variable and make it equal to empty string
    reverse1 = ""
    #Here we make a loop that will go through every element in a 
    for i in range(0, len(a), 1):
        #Here we make an element of a equal to reverse
        reverse = a[i]
        #Here we make another loop that will go through every letter in the reverse string
        #from the back of the string to the front
        for i in range(len(reverse)-1, -1, -1):
            #Here we set reverse1 equal every letter that was "i" and because it is going
            #from the back to the front it will make a new word backwards
            reverse1 = reverse1 + reverse[i]
    #Here we store the value of reverse1
    return reverse1
#Testing
print(reverseWordB(["cat","dog"]))
