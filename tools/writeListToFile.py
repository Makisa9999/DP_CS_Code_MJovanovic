def writeListToFile(name,a,state):

	file = open("test.txt", "w")
	for i in range(len(a)):
		file.write(a[i] + "\n")

	file.close()


strings = ["dad", "mom", "cat", "tree"]

writeListToFile("test.txt", strings, "w")