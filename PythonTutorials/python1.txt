# CASTING
x = str(3) # This casts variable x into a string
y = int(3) # This casts variable y into a integer
z = float(3) # This casts variable z into a float
# X and x are not the same variables, reason for this is because capital X and small x have different 
# binary code.

# GETTING TYPE OF AN VARIABLE
print(type(x)) # This will return type of x which will result in a string
print(type(y)) # This will return type of y which will result in a integer
print(type(z)) # This will return type of z which will result in a float

# NAMING VARIABLES
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# Multi words variable names can be made:
# 1. Using Camel Case which means that you will put the first letter small and then on the beginning of every
#    other word, you will start with a capital letter: myVariableName
# 2. Using Pascal Case which means that letter on beggining of every word is capital: MyVariableName
# 3. Using Snake Case, which means that you will use every an underscore between every word.

# NAMING MULTIPLE VARIABLES AT ONCE AND ASSIGNING VALUES
X, Y, Z = "Orange", "Banana", "Strawberry"
print(X, Y, Z)
# You can assign the same value for multiple variables
# X = Y = Z = "Orange"

# UNPACKING A COLLECTION
fruits = ["Orange", "Banana", "Strawberry"]
xx, yy, zz = fruits
print(xx, yy, zz)

# OUTPUT VARIABLES
Xx = "awesome"
print("You are " + Xx)

# GLOBAL VARIABLES
xX = "awesome"

def function1 ():
    print("Python is " + xX)

function1()

xxx = "awesome"

def function2 ():
    xxx = "fantastic"
    print("Python is " + xxx)

function2()

print("Python is " + xxx)

def function3 ():
    global xxX
    xxX = "Mario"

function3()

print("Python is " + xxX)

xXx = "awesome"

def function4 ():
    global xXx 
    xXx = "fantastic"

function4()

print("Python is " + xXx)

# MEMORY TYPE
# Text Type:	    str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	    dict
# Set Types:	    set, frozenset
# Boolean Type:	    bool
# Binary Types:	    bytes, bytearray, memoryview

# SETTING THE DATA TYPES
# x = "Hello World!"                                str
# x = 20                                            int
# x = 20.5                                          float
# x = 1j                                            complex
# x = ["apple", "banana", cherry]                   list
# x = ("apple", "banana", "cherry", "Mario")        truple
# x = range(6)                                      range
# x = {"name" : "Mario", "lastname" : "Jovanovic"}  dictionary
# x = {"apple", "banana", strawberry}               set
# x = forzenset({"Mario", "Jovanovic", "Apple"})    frozenset
# x = True / False                                  boolean
# x = b"Mario"                                      bytes
# x = bytearray                                     bytearray
# x = x = memoryview(bytes(5))                      memoryview

# SETTING A SPECIFIC DATA TYPE
# x = str("Hello World")	                    str	
# x = int(20)	                                int	
# x = float(20.5)	                            float	
# x = complex(1j)	                            complex	
# x = list(("apple", "banana", "cherry"))	    list	
# x = tuple(("apple", "banana", "cherry"))	    tuple	
# x = range(6)	                                range	
# x = dict(name="John", age=36)	                dict	
# x = set(("apple", "banana", "cherry"))	    set	
# x = frozenset(("apple", "banana", "cherry"))	frozenset	
# x = bool(5)	                                bool	
# x = bytes(5)	                                bytes	
# x = bytearray(5)	                            bytearray	
# x = memoryview(bytes(5))	                    memoryview

# THIS IS JUST IMPORTING A MATH MODULE
import random
# This prints out a random number everytime a program is running
print(random.randrange(1, 10))

# SPECIFY A VARIABLE TYPE
# To int 
# x = int(1)   # x will be 1
# y = int(2.8) # y will be 2
# z = int("3") # z will be 3
# To float 
# x = float(1)     # x will be 1.0
# y = float(2.8)   # y will be 2.8
# z = float("3")   # z will be 3.0
# w = float("4.2") # w will be 4.2
# To str
# x = str("s1") # x will be 's1'
# y = str(2)    # y will be '2'
# z = str(3.0)  # z will be '3.0'

multiLineString = """
Hello
This
Is
A
Multi
Line
String
"""
print(multiLineString)

# ACCESSING LETTERS IN STRINGS
#      0123456789...
# a = "Hello World!"
# print(a[0]) This will just print out H

# LOOPING THROUGH STINGS
for i in "banana":
    print(i)

# YOU CAN GET STRING LENGHT BY USING FUNCTION LEN()
A = "Mario Jovanovic"
print(len(A))

# YOU CAN CHECK IF THERE IS A WORD IS SOME STRING
txt = "My name is Mario Jovanovic. I am 20 years old."
print("name" in txt)
# We can do the same with an if statement
if "name" in txt:
    print('Yes, word "name" is present!')
# Also we can check if something is not in the string
print("mama" not in txt)
# Another way with if statement
if "mama" not in txt:
    print('"Mama" is not present in text!')

# SLICING STRINGS
bb = "Hello World!"
# Here letter with index of 2 is included and letter with index of 5 is excluded
print(bb[2:5])
# Here we can see faster notation to writing from the beginning of the string to index 5 excluded.
print(bb[:5])
# Here we can see faster notation to writing from the letter at index 2 included to the end of the string
print(bb[2:])
# We could also use negative indexes to slice words from the end for example, from the fifth character
# from behind to the second from behind.
print(bb[-5:-2])

# MODIFY STRINGS
# .upper() - switch every letter to uppercase
# .lower() - switch every letter to lowercase
# .strip() - removes whitespace from the beginning and end
# .replace(".", ",") - here this function takes two parameters, which character are you changing and to
#                      what are you changing it.
# .split() - here this function will split the string on every space and make a list of the splitted elements

# STRING CONCATENATION
# A = "Mario"
# B = "Jovanovic"
# C = A + B
# print(C) // This will return MarioJovanovic
# We can add a space between my name and lastname just by rewriting this:
# C = A + " " + B
# print(C) // This will return Mario Jovanovic

# FORMATING STRINGS
# Here we used function format() to insert a number 35 into a string on a place where we put {}
age = 35
txt123 = "Hello, my name is Mario and I am {} years old."
print(txt123.format(age))
# You can put multiple values in one string at once
age1 = 35
quantity = 23
price = 19.99
txt12 = "Hello, my name is Mario and I am {} years old. I want to buy {} pieces by the price of {} dollars."
# Here values in the sentence will be displayed first age1, then quantity, then price.
print(txt12.format(age1, quantity, price))
# We can put them in different order by putting a number between the brackets.
txt1 = "Hello, my name is Mario and I am {2} years old. I want to buy {1} pieces by the price of {0} dollars."
print(txt1.format(age1, quantity, price))

# ESCAPE CHARACTERS
# They give you a permission to make double quotes where you can't, so now you can nest double quotes in sentence.
string = "Nadimak Mariu Jovanovicu je \"Makisa\"."
print(string)
# Other things you can put in your sentence:
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

# STRING METHODS
# capitalize()	    Converts the first character to upper case
# casefold()	    Converts string into lower case
# center()	        Returns a centered string
# count()	        Returns the number of times a specified value occurs in a string
# encode()	        Returns an encoded version of the string
# endswith()	    Returns true if the string ends with the specified value
# expandtabs()	    Sets the tab size of the string
# find()	        Searches the string for a specified value and returns the position of where it was found
# format()	        Formats specified values in a string
# format_map()	    Formats specified values in a string
# index()	        Searches the string for a specified value and returns the position of where it was found
# isalnum()	        Returns True if all characters in the string are alphanumeric
# isalpha()	        Returns True if all characters in the string are in the alphabet
# isdecimal()	    Returns True if all characters in the string are decimals
# isdigit()	        Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	        Returns True if all characters in the string are lower case
# isnumeric()	    Returns True if all characters in the string are numeric
# isprintable()	    Returns True if all characters in the string are printable
# isspace()	        Returns True if all characters in the string are whitespaces
# istitle()	        Returns True if the string follows the rules of a title
# isupper()	        Returns True if all characters in the string are upper case
# join()	        Joins the elements of an iterable to the end of the string
# ljust()	        Returns a left justified version of the string
# lower()	        Converts a string into lower case
# lstrip()	        Returns a left trim version of the string
# maketrans()	    Returns a translation table to be used in translations
# partition()	    Returns a tuple where the string is parted into three parts
# replace()	        Returns a string where a specified value is replaced with a specified value
# rfind()	        Searches the string for a specified value and returns the last position of where it was found
# rindex()	        Searches the string for a specified value and returns the last position of where it was found
# rjust()	        Returns a right justified version of the string
# rpartition()	    Returns a tuple where the string is parted into three parts
# rsplit()	        Splits the string at the specified separator, and returns a list
# rstrip()	        Returns a right trim version of the string
# split()	        Splits the string at the specified separator, and returns a list
# splitlines()	    Splits the string at line breaks and returns a list
# startswith()	    Returns true if the string starts with the specified value
# strip()	        Returns a trimmed version of the string
# swapcase()	    Swaps cases, lower case becomes upper case and vice versa
# title()	        Converts the first character of each word to upper case
# translate()	    Returns a translated string
# upper()	        Converts a string into upper case
# zfill()	        Fills the string with a specified number of 0 values at the beginning

# BOOLEANS
# True or False
number1 = 12
number2 = 10
print(number1 > number2)
boolean1 = True
boolean2 = False
# The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("M"))
# Every string is True except empty string ""
print(bool(""))
print(bool(2))
# Every number is True except 0
print(bool(0))
print(bool(["Mario", "Jovanovic", "23"]))
#Every list, truple, set, dictionary is True except empty list
print(bool([]))
# One more value, or object in this case, evaluates to False, and that is if you have an object that 
# is made from a class with a __len__ function that returns 0 or False:
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

def function5():
    return True
print(function5())

# This is an if statement that will print Yes if the function5 returns true and it will print no for 
# everything else
if function5(): 
    print("Yes")
else:
    print("No")

# Python also has many built-in functions that return a boolean value, like the isinstance() function, 
# which can be used to determine if an object is of a certain data type:

number3 = 200
# isinstance takes 2 parameters, first one is the value, and second one is a type which you compare the 
# the value to.
print(isinstance(x, int))

# PYTHON ARITHMETIC OPERATORS
# +	    Addition	    x + y	
# -	    Subtraction	    x - y	
# *	    Multiplication	x * y	
# /	    Division	    x / y	
# %	    Modulus	        x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y

# =	    x = 5	    x = 5	
# +=	x += 3	    x = x + 3	
# -=	x -= 3	    x = x - 3	
# *=	x *= 3	    x = x * 3	
# /=	x /= 3	    x = x / 3	
# %=	x %= 3	    x = x % 3	
# //=	x //= 3	    x = x // 3	
# **=	x **= 3	    x = x ** 3	
# &=	x &= 3	    x = x & 3	
# |=	x |= 3	    x = x | 3	
# ^=	x ^= 3	    x = x ^ 3	
# >>=	x >>= 3	    x = x >> 3	
# <<=	x <<= 3	    x = x << 3

# ==	Equal	                    x == y	
# !=	Not equal	                x != y	
# >	    Greater than	            x > y	
# <	    Less than	                x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	    x <= y

# and 	Returns True if both statements are true	                x < 5 and  x < 10	
# or	Returns True if one of the statements is true	            x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)

# is 	    Returns True if both variables are the same object	    x is y	
# is not	Returns True if both variables are not the same object	x is not y

# in 	    Returns True if a sequence with the specified value is present in the object	    x in y		
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

# & 	AND	                    Sets each bit to 1 if both bits are 1
# |	    OR	                    Sets each bit to 1 if one of two bits is 1
# ^	    XOR	                    Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT	                    Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost 
#                               bits fall off
# >>	Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, 
#                               and let the rightmost bits fall off

# PYTHON LISTS
thislist = ["apple", "banana", "cherry"]
print(thislist)
# Lists allow duplicate values
thislist1 = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
# You can find the lenght of a list
thislist2 = ["apple", "banana", "cherry"]
print(len(thislist))
# Lists accept strings, numbers, booleans, also they accept mixtures of all
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
# Returns a type of mylist
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
# This is another way that you can make a list
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
# Prints the value in thislist at value 0
print(thislist[0])
# Prints the value in this list at value -2
print(thislist[-2])
newList = ["Mario", "Jovanovic", "2131", "Marko", "Mark", "Nemanja"]
# You can print values from index 2 inclusive to 5 exclusive
print(newList[2:5])
print(newList[2:])
print(newList[:5])
print(newList[-4:-1])
if "Mario" in newList:
    print("Yes, 'Mario' is in the fruits list")
# You can change the values in a list by accessing it
newList[1] = "Jovanovic22"
print(newList)
thislist22 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist22[1:3] = ["blackcurrant", "watermelon"]
print(thislist22)
# You can replace one element with two
thislist222 = ["apple", "banana", "cherry"]
thislist222[1:2] = ["blackcurrant", "watermelon"]
print(thislist222)
# You can replace two elements with one
thislista = ["apple", "banana", "cherry"]
thislista[1:3] = ["watermelon"]
print(thislista)
# You can just insert a value in a list
thislistb = ["apple", "banana", "cherry"]
thislistb.insert(2, "watermelon")
print(thislistb)
# You can append a element to the end of the list
thislistc = ["apple", "banana", "cherry"]
thislistc.append("orange")
print(thislistc)
# You can insert a value on index 1
thislistd = ["apple", "banana", "cherry"]
thislistd.insert(1, "orange")
print(thislistd)
# You can add two lists together
thisliste = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thisliste.extend(tropical)
print(thisliste)
# Add elements of a tuple to a list
thislistf = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislistf.extend(thistuple)
print(thislistf)
# You can remove this element "banana"
thislist1221 = ["apple", "banana", "cherry"]
thislist1221.remove("banana")
print(thislist1221)
# You can remove the second item from the list
thislist12211 = ["apple", "banana", "cherry"]
thislist12211.pop(1)
print(thislist12211)
# This will remove the last element from the list
thislist12211.pop()
print(thislist12211)
# This will remove the only element in the list
del thislist12211[0]
print(thislist12211)
# This will remove the list so you will not be able to print it.
del thislist12211
# This will clear the list and remove every single element from it.
newList1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
newList1.clear()
print(newList1)

# LOOP THROUGH THE LIST
