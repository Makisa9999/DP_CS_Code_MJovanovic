# You open the file
file = open("DP_CS_Code_MJovanovic/StackOverflow/text.txt")
# You read the whole file and put it in a list where each line would be one 
# item in the list.
readFile = file.read().split("\n")
# Set a new variable so you can concatinate a string
text = ""
# Loop through the list of rows
for i in range(0, len(readFile), 1):
    # Concatinate the each row into one string and add a comma and a space.
    text = text + readFile[i] + ", "
# Print the text
print(text)