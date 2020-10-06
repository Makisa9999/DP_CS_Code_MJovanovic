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


#Here we make a new function called perfectNumberFinder that is going to take parameter number
def perfectNumberFinder (number):
    #Here we create a new list that is going to be empty
    #Lists - A list is a dynamic data structure in Python that is a mutable, or changeable, 
    # ordered sequence of elements. Each element or value that is inside of a list is called an item. 
    lst = []
    #Here we make a new variable called n and make it equal to 0
    n = 0
    #Here we make a new variable called suma and make it equal to 0
    suma = 0
    #Here we make a new list called perfectNumberslst and make it empty
    #Lists - A list is a data structure in Python that is a mutable, or changeable, ordered sequence
    #        of elements. Each element or value that is inside of a list is called an item.
    perfectNumberslst = []
    #Here we have a while loop which is going to preform two tests first is always true and 
    #other test will be true only if n is less than 10000
    while True and n < 10000:
        #Here we add 1 to n each time it passes through this while loop
        #Self referencing assignment statements - Self referencing assignment statements are statements
        #                                          which add some value to the existing value. Like 
        #                                          X = X + 3 + 1
        n = n + 1
        #Here we make a if statement which is true if the remainder of number divided with n is 
        #equal to 0
        if number % n == 0:
            #If the test is true, then we append n value to that list
            #Instance Functions - Does have an implied object. lst.append(5) is an instance function because
            #                     it needs to refer to something in this case lst
            lst.append(n)
    #Here we have a loop that is going to go through every single element in our lst list from
    #from the first one to the last one
    #Standard loop to go throught front to back or back to front - for i in range(0,len(str),1):
    for i in range(0, len(lst), 1):
        #Here we add the number from the lst list each time we pass through the loop
        #Self referencing assignment statements - Self referencing assignment statements are statements
        #                                          which add some value to the existing value. Like 
        #                                          X = X + 3 + 1
        suma = suma + lst[i]
        #Here we test with an if statement if the suma is equal to the number we put in function
        if suma == number:
            #Here if suma is equal to the number than we append it to the perfectNumberslst
            #Instance Functions - Does have an implied object. lst.append(5) is an instance function because
            #                     it needs to refer to something in this case lst
            perfectNumberslst.append(number)
            #Here we return the perfectNumberslst
            return perfectNumberslst
#Testing:
print(perfectNumberFinder(6))
print(perfectNumberFinder(21))
print(perfectNumberFinder(-1))
print(perfectNumberFinder(28))
print(perfectNumberFinder(2.1))

#Example 1: number == 6 TRACE TABLE                                [i]
# |    while     | n |     if     |     lst     | for i in range | list | suma |  perfect  |
# | True n == 0  | 1 | 6 % 1 == 0 |     [1]     |                |      |      |           |
# | True n == 1  | 2 | 6 % 2 == 0 |    [1,2]    |                |      |      |           |
# | True n == 2  | 3 | 6 % 3 == 0 |   [1,2,3]   |                |      |      |           | 
# | True n == 3  | 4 | 6 % 4 == 2 |   [1,2,3]   |                |      |      |           | 
# | True n == 4  | 5 | 6 % 5 == 1 |   [1,2,3]   |                |      |      |           |
# | True n == 5  | 6 | 6 % 6 == 0 |  [1,2,3,6]  |                |      |      |           |
# | True n == 6  | 7 | 6 % 7 == 6 |  [1,2,3,6]  |                |      |      |           | 
# |      ...     |...|     ...    |     ...     |                |      |      |           | 
# |True n==10000 |9999| 6 % 7 == 6|  [1,2,3,6]  |                |      |      |           |
# |              |   |            |             |       0        |  1   |   1  |    []     |
# |              |   |            |             |       1        |  2   |   3  |    []     |
# |              |   |            |             |       2        |  3   |   6  |    [6]    |

# Pseudocode
# LST = []
# N = 0
# SUMA = 0
# PERFECTNUMBERSLST = []
# loop while is TRUE and N < 10000:
#     N = N + 1
#     loop if NUMBER mod N = 0:
#         LST.append(N)
#     end if
# end while
# loop I from 0 to LST.lenght by 1:
#     SUMA = SUMA + LST[I]
#         if SUMA = NUMBER:
#             PERFECTNUMBERSLST.append(NUMBER)
#             output PERFECTNUMBERSLST
#         end if 
# end loop


