#Casting is the process of changing types.
#Primitive types - These variable types store data at the location in the memory.
#Reference types - These variable types store a reference to data in the memory location.
#Variables memory - Python refers to the memory, that means when we call a variable it tells
#                   us where did it store the value.
#                   Integers are 32 bit variables.
#Static data structure - Size must be declared in advance and it can't change(ARRAYS).
#Dynamic data structure - Size can change.
#Improtance of commenting - For your own understanding, For the understanding of working in the
#                           team, For being consistent in approach, When sharing code to a larger
#                           community. 
#What is a high level language? - The further you move from the machine language the higher the 
#                                 language, This means that the more you use English to write 
#                                 code the higher the language. 
#Data structures - Lists, Arrays, Dictionaries, Dynamic vs Static, indexes and elements,
#                  The standard loop to go through front to back, back to front.
#Lists - A list is a data structure in Python that is a mutable, or changeable, ordered sequence
#        of elements. Each element or value that is inside of a list is called an item.
#Arrays - An array is a data structure that stores values of same data type. In Python, 
#         this is the main difference between arrays and lists. While python lists can contain 
#         values corresponding to different data types, arrays in python can only contain values 
#         corresponding to same data type.
#Dictionaries - A dictionary is a collection which is unordered, changeable and indexed. 
#               In Python dictionaries are written with curly brackets, and they have keys and 
#               values.
#Indexes - An index, in your example, refers to a position within an ordered list. Python strings 
#          can be thought of as lists of characters; each character is given an index from zero 
#          (at the beginning) to the length minus one (at the end).
#          0 1 2 3 4 5
#          P y t h o n
#Elements - Elements are just part of a list.
#Standard loop to go throught front to back or back to front - for i in range(0,len(str),1):
#Assignment statements - Assignment statements are statements which store a value in a new 
#                        variable. Like X = 3 + 1
#Self referencing assignment statements - Self referencing assignment statements are statements
#                                         which add some value to the existing value. Like 
#                                         X = X + 3 + 1
#Trace tables - Trace tables are tables that help you track what is your code doing. You 
#               should include tracetables in the video by making them in advance.
#Functions - Parameters, Return Types, Preconditions, Postconditions, Abstractions, 
#            Static function, Instance fucntions, Reference in terms of functions, strings
#Parameters - Inforamtion that are passed into a function
#Return types - defines and constrains the data type of the value returned from a subroutine or 
#               method. In python we can return numeric values non-numeric values, boolean values
#Preconditions - A precondition is something that must be true at the start of a function in 
#                order for it to work correctly.
#Postconditions - A postcondition is something that the function guarantees is true when it 
#                 finishes.
#Abstraction - Abstraction is the process of hiding the real implementation of an application 
#              from the user and emphasizing only on usage of it.
#Static Functions - Does not have an implied object. Like max(lst) is static function because 
#                   it doesn't need anything to refer to.
#Instance Functions - Does have an implied object. lst.append(5) is an instance function because
#                     it needs to refer to something in this case lst
#Reference in terms of functions - Every list in a function is stored as a reference to a value
#                                  it says where is that value stored.
#Strings - Strings are bytes of data representing different characters


'''
Tool 1:

Write a tool called mergeStrings. To merge the lists the method should add strings in the 
same index together in any order. If one list is longer than the other the none paired 
indexes should be included in c.    

If a[0] = “cat” and b[0] = “dog” then c[0] = “catdog” or “dogcat”.  
If a[n] = “one” and b has no index n then c[n] = “one”. 
If b[n] = “one” and a has no index n then c[n] = “one”

Parameters: String[] a, String[] b
Return: String[]

Preconditions: none
Postconditions: The two passed lists remain unchanged. 

mergeStrings([“cat”,”dog”,”fish”],[“one”]) → [“catone”,”dog”,”fish”]
mergeStrings([“red”,”green”],[“six”,”seven”] → [“redsix”,greenseven”]
mergeStrings([],[“one”,”two”,”three”] → [“one”,”two”,”three”]
'''
#Here we are making a new function called mergeStrings and it takes parameters a and b
def mergeStrings(a,b):
    #Here we made a new variable that is going to be an integer and going to store the lenght 
    #of a

    lenghta = len(a)
    #This is a new variable that is going to be an integer and going to store the lenght of b
    lenghtb = len(b)
    #This is a new variable that is an empty string
    empty = ""
    #This is a new variable called c and it is going to be an empty list
    c = []
    #This is going to be a new variable and it is going to be equal to 0
    diff = 0
    #This is an if statement that tests if the lenght of list a is equal to the lenght of the
    #list b
    if lenghta == lenghtb:
        #This is a for loop which is going to go through every element in the list a starting at
        #front and continuing to the back by 1
        for i in range(0, lenghta, 1):
            #Here we are storing a at i and b at i in one string. This means that here we are 
            #adding strings. 
            empty = a[i] + b[i]
            #Here we are going to put this string called empty in the list that is called c
            c.append(empty)
        #Here we are storing the value of c
        return c
    #Here we are testing another case when list a is longer than list b
    elif lenghta > lenghtb:
        #Here we are calculating the difference between the shorter list and the longer one
        #so that later we would know how many elements should we put in the new list c
        diff = lenghtb - lenghta
        #This is a for loop that is going to go through every element of list b starting at front
        #all the way through the back
        for i in range(0, lenghtb, 1):
            #Here we are storing a at i and b at i in one string. This means that here we are 
            #adding strings.
            empty = a[i] + b[i] 
            #Here we are adding that empty string to the list c
            c.append(empty)
        #Now we need to add those left parts of the list in c. We do that by making a while loop 
        #that is going to be true if difference is less than 0.
        while diff < 0:
            #Here we add an item to the list that is going to be located on the index diff. 
            #Difference is calculated above.
            c.append(a[diff])
            #We are adding one to difference because we want to end the loop when all the elements 
            #were added to the list c
            diff = diff + 1
        #Storing the value of c
        return c
    #Here we are testing if the lenght of a is smaller than lenght of b.
    elif lenghta < lenghtb:
        #Here we are storing the difference in lenghts in variable called diff
        diff = lenghta - lenghtb
        #Here we are looping through every single element in the list a starting from the first 
        #one and ending at the last one
        for i in range(0, lenghta, 1):
            #Here we adding two strings in the list a and b and storing it in variabe called empty
            empty = a[i] + b[i]
            #Here we are adding empty to the end of the list c
            c.append(empty)
        #We are testing if the difference is less than 0 if it is than we are continuing the loop
        while diff < 0:
            #We are adding the string b at value diff
            c.append(b[diff])
            #Incrementing the variable diff by one each time we run loop
            diff = diff + 1
        #Storing the value of c
        return c

#Testing
print(mergeStrings(["boat", "cano", "bread", "stapler", "calculator"], ["water", "wine"]))
print(mergeStrings(["water", "wine"], ["boat", "cano", "bread", "stapler", "calculator"]))
print(mergeStrings(["boat", "cano", "bread", "stapler", "calculator"], ["boat", "cano", "bread", "stapler", "calculator"]))
print(mergeStrings([],["boat", "cano", "bread", "stapler", "calculator"]))
print(mergeStrings(["boat", "cano", "bread", "stapler", "calculator"], []))

#Flowchart:
#https://drive.google.com/drive/u/0/folders/12U7p8gl-aBPskwzlngs8yk6VK_jHFBKk

# Pseudocode
# LENGHTA = A.lenght
# LENGHTB = B.lenght
# EMPTY = ""
# C = []
# DIFF = 0
# if LENGHTA = LENGHTB:
#     loop for I from 0 to LENGHTA by 1:
#         EMPTY = A[I] + B[I]
#         C.append(EMPTY)
#     end loop
# elif LENGHTA > LENGHTB:
#     DIFF = LENGHTB - LENGHTA
#     loop for I from 0 to LENGHTB by 1:
#         EMPTY = A[I] + B[I]
#         C.append(EMPTY)
#     end loop
#     loop while DIFF < 0:
#         C.append(A[DIFF])
#         DIFF = DIFF + 1
#     end while
# elif LENGHTA < LENGHTB:
#     DIFF = LENGHTA - LENGHTB
#     loop for I from 0 to LENGHTA by 1:
#         EMPTY = A[I] + B[I]
#         C.append(EMPTY)
#     end loop
#     loop while DIFF < 0:
#         C.append(B[DIFF])
#         DIFF = DIFF + 1
#     end while
# end if

'''
Tool 2:

Write any tool that incorporates the concept of a linear search.  A linear search is an 
algorithm that moves through a data structure in sequential order with the goal of identifying 
a specific element or elements. We have written a number of these structures in our examples 
from class, just never called them a linear search.  You can find further information here,

https://www.geeksforgeeks.org/linear-search/

As long as the tool has a linear search the tool can be whatever you want. 

This tool is going to find a number that you enter as a test case in the list provided.
            TEST              OUTPUT
print(linearFunction(21)) --> True 
print(linearFunction(51)) --> False
'''
#Here we are creating a new function called linearFunction that is going to take parameter a
def linearSearch (a):
    #Here I made a list called n and it has values below
    n = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
    #Here I make a new variable that is a boolean value and make it equal to false
    find = False
    #Here I use the loop that is going to go through every element in the n list 
    for i in range(0, len(n), 1):
        #Here is an if statement that is going to check if n at i is equal to a
        if n[i] == a:
            #If the test is passed then it will change the boolean values to equal to True
            find = True
    #Here I will just return the value
    return find
#Testing:
print(linearSearch(0))
print(linearSearch(12))
print(linearSearch(23))
print(linearSearch(51))

#Flowchart
#https://drive.google.com/drive/u/0/folders/12U7p8gl-aBPskwzlngs8yk6VK_jHFBKk


# Pseudocode:
# function linearSearch parameter A:
# N = [0,1,2,3,4,5,6,7,8,9,10...49,50]
# FIND = False
# loop for I from 0 to N.lenght by 1:
#     if N[I] == A:
#         find = True
#     end if
# end loop

'''
Tool 3:

Write any tool that incorporates a dictionary. A dictionary is the data structure we explored 
when pulling data from an API. You can find syntax information for Python here,

https://www.w3schools.com/python/python_dictionaries.asp

As long as the tool uses a dictionary in some format any submission is acceptable. This includes 
passing a dictionary, returning a dictionary or both.

This function is going to let you enter a color in test cases and it is going to bring it 
back with a better explanation what that color looks like.
'''
#Here we make a function that is called dictionaryColors that takes parameters s
def dictionaryColors(s):
    #Here we make a new variable that is going to an empty string
    result = ""
    #Here we are making a new dictionary called carColors, it has parameters that are connected
    #inside
    carColors = { 
        "apricot": "orange",
        "peach": "orange",
        "maroon": "dark red",
        "violetred": "pink",
        "greenyellow": "lightgreen",
        "goldenrod": "goldenyellow",
        "dandelion": "lightorange"
    }
    #Here is a standard loop that is going to go through every element in the dictionary.
    for i in range(0, len(s), 1):
        #Here we are making the result equal the color of the key which is going to be translated 
        #then to be equal to the color that the key represents, which is going to be printed out on 
        #the screen
        result = carColors[s]
    #Exiting the function and handing back the value result
    return result
#Testing
print(dictionaryColors("peach"))
print(dictionaryColors("maroon"))
print(dictionaryColors("violetred"))
print(dictionaryColors("apricot"))
print(dictionaryColors("greenyellow"))
print(dictionaryColors("goldenrod"))
print(dictionaryColors("dandelion"))

#Flowchart:
#https://drive.google.com/drive/u/0/folders/12U7p8gl-aBPskwzlngs8yk6VK_jHFBKk

# Pseudocode:
# function called dictionaryColors parameter S:
# RESULT = ""
# CARCOLORS = {
#   item1 "apricot" = "orange"
#   item2 "peach" = "orange"
#   item3 "maroon" = "dark red"
#   item4 "violetred" = "pink"
#   item5 "greenyellow" = "lightgreen"
#   item6 "goldenrod" = "goldenyellow"
#   item7 "dandelion" = "lightorange"
#   loop for I from 0 to S.lenght by 1:
#       result = carColors[s]
#   end loop 


