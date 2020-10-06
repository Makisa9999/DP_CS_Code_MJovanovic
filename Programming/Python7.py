'''
I wanted to make a program that is going to find a largest number in the list and print it out.
Right here we made a list with random numbers.
numb = [1, 3, 5, 21, 3, 5, 8, 2]

Here we used .sort() element to sort these numbers from smallest to the largest. 
numb.sort()

Because the computer sorted the numbers from smallest to largest now we just need to print the last number in the list.
print(numb[-1])

Here we can see the list of numbers. 
numbers = [1,2,3,4,5,63,12,32,56,21]

Here we created a new variable that is going to hold the first number in the list.
max = numbers[0]
#Here we created a for loop to check every number in the list
for number in numbers:
    #Here is the if statement to test if the number that we stored in the max value is bigger than the next number in the list
    if number > max:
        #Here if the test is true we will have that new bigger number stored in the max variable
        max = number
#This is just a line to print out the max number.
print(max)

#Python can store values by integers.
price = 10

#store values by floats
price1 = 4.99

#store values by string
name = "Mario"

#store values by booleans
in_booleans = True

#Here we print out Welcome to hospital!
print("Welcome to hospital!")

#This is the name of the patient
patient = "John Smith"

#This is the name of the patient
yearsOld = 20

#This will say if this is a new patient
first_time = True

#We are searching for a input from the user
name = input("What is your name: ")

#Right here we have an input and we want to print out "Hello Mr. " and the name that has been taken from the user.
print("Hello Mr. " + name)

#Challenge
name = input("What is your name? ")
favourite_color = input("What is your favourite color? ")
favourite_color = favourite_color.lower()
print("This is " + name + ". His favourite color is " + favourite_color + ".")
#Challenge completed

#Challenge
current_Year = 2020
birth_Year = int(input("What year were you born? "))
years_Old = current_Year - birth_Year
print(years_Old)
#Challenge completed

#Challenge
kg = input("What is your weight in kg? ")
lbs = int(kg) * 2.204622622
print(lbs)
#Challenge completed

#If you want to put in the " ' " in the sentence when you are writing. You will need to start the string with ("") 
#If you use ' it wont break a string the same works on reverse.
print("So you can use ' as much as you want ' ' ' ' ' ' '")


#If you want to print multi line strings you will need to write """ three of these.
email = """
Dear Mr. Mario,
I would like to inform you about the delivery of your new bike.

Sincereely,
Nenad
"""
print(email)

#Formatted strings
#String holds my name and surname
first = "Mario"
last = "Jovanovic"
#This is an ordinary way to writeout text on screen
message = first + " [" + last + "] is a coder." 
#This is a special way to writeout text on screen, it gives the same output
message1 = f"{first} [{last}] is a coder."
#this is just to print out
print(message)
print(message1)

#This is a string with a value
course = "Python for Biginners!"
#This will printout the lenght of course
print(len(course))
#This will print course in lowercase letters
print(course.lower())
#This will print course in uppercase letters
print(course.upper())

#How to find a character in the string.
course_1 = "Python for Biginners!"
#This will print out the first occurance of letter "n" in course_1 string
print(course_1.find("n"))
#This will print the index where word Biginners start.
print(course_1.find("Biginners!"))
#If you want to replace some letter with another, or a word with another there is a built in function for that.
print(course_1.replace("Biginners", "Absolute Biginners"))
#This will count the letters in Python for Biginners. If we want to store a new value and calculate the length of Python for 
#Absolute Biginners we need to store a new value in course_1
print(len(course_1))
#Here we are storing a new value in course_1 where we replace the word Biginners with Absolute Biginners
course_1 = course_1.replace("Biginners" , "Absolute Biginners")
#Here we are just counting the number of letters in new string course_1
print(len(course_1))
#Here we are printing the new string
print(course_1)
#This will print out the boolean value if the word Python is in course_1
print("Python" in course_1)
#Takes every first letter in a word and makes it uppercase
print(course_1.title())

#Here we are putting value of 10 in x
x = 10
#Here we are incrementing it by 1
x = x + 1
#Here we are incrementing it by 1 again but in a different way.
x += 1

#Here we import math operations so we can use them as dot operators
import math
#Here we set value of x to -2.9
x = -2.9
#here we print that value and then round it and then make it an absolute value
print(round(abs(x)))
'''
