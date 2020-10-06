
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
#Functions are blocks of code that only run when called. You can pass data into function known as
#parameters
def mergeStrings(a,b):
    #Here we made a new variable that is going to be an integer and going to store the lenght 
    #of a
    #This is a built-in function that finds the lenght of a string,by starting at the first index
    #of a string and going to the last one. len is a static function because there is no implied 
    #object.
    lenghta = len(a)
    #This is a new variable that is going to be an integer and going to store the lenght of b
    lenghtb = len(b)
    #This is a new variable that is an empty string
    empty = ""
    #This is a new variable called c and it is going to be an empty list
    #Lists are dynamic data structures.
    c = []
    #This is going to be a new variable and it is going to be equal to 0
    diff = 0
    #This is an if statement that tests if the lenght of list a is equal to the lenght of the
    #list b
    #If function are function which are run when certain condition is true, if it is not true, 
    #then it will run the code under else statement.
    if lenghta == lenghtb:
        #This is a for loop which is going to go through every element in the list a starting at
        #front and continuing to the back by 1
        #For loops are used for iterating over a sequence. Could be a list, string, array...
        for i in range(0, lenghta, 1):
            #Here we are storing a at i and b at i in one string. This means that here we are 
            #adding strings. 
            #Assignment statements - Assignment statements are statements which store a value in
            #                        a new variable. Like X = 3 + 1
            empty = a[i] + b[i]
            #Here we are going to put this string called empty in the list that is called c
            #Instance function - It has an implied object 
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
        #While loop can execute more statements as long as condition is true.
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
