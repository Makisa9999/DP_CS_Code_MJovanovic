'''
Yesterday, (name1) and I had a computer science class. In this class we reviewed all 
(number1) criteria that we would be assessed on. I realized that this is going to be a 
(adjective1) task for me to complete so I will have to start early. Our class is located 
in a (adjective2) classroom number (number2). There are going to be a lot of (adjective3) 
classes where I could ask my professor if I had any (adjective4) questions. My professor 
told me that I will need to spend around (number 3) hours in order to finish my internal 
assessment. 
'''
# Asking for inputs
name1 = input("Yesterday, ________ (name) and I had a computer science class. \n\n")
number1 = input("In this class we reviewed all _______ (number) criteria that we would be assessed on. \n\n")
adjective1 = input("I realized that this is going to be a __________ (adjective) task for me to complete so I will have to start early. \n\n")
adjective2 = input("Our class is located in a ________ (adjective) classroom number (number). \n\n")
number2 = input("Our class is located in a " + adjective2 + " classroom number __________ (number). \n\n")
adjective3 = input("There are going to be a lot of ___________ (adjective) classes where I could ask my professor if I had any (adjective) questions. \n\n")
adjective4 = input("There are going to be a lot of " + adjective3 + " classes where I could ask my professor if I had any ____________ (adjective) questions. \n\n")
number3 = input("My professor told me that I will need to spend around ___________ (decimal number) hours in order to finish my internal assessment. \n\n")
# Casting the number from a string into a integer or a float.
number1 = int(number1)
number2 = int(number2)
number3 = float(number3)
# Printing the final sentence.
finalAnswer = "Yesterday, " + name1 + " and I had a computer science class. In this class we reviewed all " + str(number1) + " criteria that we would be assessed on. I realized that this is going to be a " + adjective1 + " task for me to complete so I will have to start early. Our class is located in a " + adjective2 + " classroom number " + str(number2) + ". There are going to be a lot of " + adjective3 + " classes where I could ask my professor if I had any " + adjective4 + " questions. My professor told me that I will need to spend around " + str(number3) + " hours in order to finish my internal assessment."
print(finalAnswer)
# Setting a new variable with boolean value False
value = False
# Asking for a string input
booleanValue = input("Is your sentence correct? True or False? \n\n")
# Testing if the input is True or False and testing if it is neither
if booleanValue == "True":
    value = True
elif booleanValue == "False":
    value = False
else:
    print("Wrong input!")
# Printing the boolean value.
print(value)
