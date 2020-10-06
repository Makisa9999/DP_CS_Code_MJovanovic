def readFileToList(name):

	#open is a function that takes two String parameters and returns 
	#a reference to a file.  Open is in Pythons standard library because
	#I can directly access it. 
	file = open("readFileToList.txt","r")

	#create a new list called result which is empty
	result = []

	#while C.hasNext():
	for line in file:
		result.append(line)
result = readFileToList("readFileToList.txt")
print(result)