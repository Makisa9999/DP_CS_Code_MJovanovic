# Read through the program on the video.
# 
# Problem Description Time on task.

# You have been asked by a parental unit to do your chores.
# Each chore takes a certain amount of time, but you may not have enough time to do all of your
# chores, since you can only complete one chore at a time. You can do the chores in any order that
# you wish.

# What is the largest amount of chores you can complete in the given amount of time?

# Input Specification

# The first line of input consists of an integer T (0 ≤ T ≤ 100000), which is the total number of
# minutes you have available to complete your chores.

# The second line of input consists of an integer C (0 ≤ C ≤ 100), which is the total number
# of chores that you may choose from. The next C lines contain the (positive integer) number of
# minutes required to do each of these chores. You can assume that each chore will take at most
# 100000 minutes.

# Output Specification

# The output will be the maximum number of chores that can be completed in time T.

# Sample Input 1

# 6
# 3
# 3
# 6
# 3

# Output for Sample Input 1

# 2

# Explanation of Output for Sample Input 1

# Chores must be completed in at most 6 minutes. There are 3 chores available. The first chore takes
# 3 minutes. The second chore takes 6 minutes. The third chore takes 3 minutes. The answer is
# 2 since only 2 of these chores can be completed in 6 minutes of time. Specifically, the first and
# last chore can be completed in the allowable time. It is not possible to complete all 3 chores in 6
# minutes.

# This first line consists of number of availiable minutes we have to do our chores.
# CASTING
time = int(input())
# This is the number of chores that we need to do.
num_chores = int(input())
# Now we can create an empty list that is going to store all times per chore we need to spend on it.
time_lst = []
# Because there is an undefined number of chores, meaning there can be 100 chores or 0 chores. We can make this as a loop which is going
# to take inputs for number of chores.
# In other words, this is going to loop and take inputs for the number of chores taht you put in.
# BIG IDEA THAT YOU CAN TAKE INPUTS THROUGH LOOPS
# Show file bigIdea.py
for i in range(num_chores):
    # This line takes the input for every chore and stores it in x.
    x = int(input())
    # This line it will take that value x and going to append it to the list.
    time_lst.append(x)

    # ONE MORE WAY WE COULD DO THIS
    # This would increase the efficiency of our program.
    #time_lst.append(int(input()))

# Here it is sorting the list from smallest to biggest, using instance function sort(), which takes time_lst as an object.
# We needed to sort this list, because if we do the chore that we need the most time, then we won't be able to get the maximum amount of
# chores done.
time_lst.sort()
#This creates a counter and i and sets them to 0. Counter is used to count the number of chores completed.
counter = 0
# i is used as a variable that is going to escape the infinite while loop.
i = 0
# This is a while loop that is going to loop until time greater or equal to time_lst[i].
while time >= time_lst[i]:
    # As we loop through the list with i variable, we are going to decrese the time that we have left, because we used some time for 
    # the first chore.
    time = time - time_lst[i]
    # We increase the counter by one to mark that we finished one chore. 
    counter = counter + 1
    # We increase the i so we can access the next chore in the list.
    i = i + 1
# At the end we just print the counter to mark the number of chores that we did.
print(counter)

# TRACE TABLE
'''
| time | num_chores | for i in range(num_chores) | x    | time_lst  | time_lst.sort() | time_lst[i] | while time >= time_lst[i] | time    | counter |   i  | print(counter) |
|  8   |      5     |               0            | 2    |[2]        |                 |             |                           |         |         |      |                |
|      |            |               1            | 3    |[2,3]      |                 |             |                           |         |         |      |                | 
|      |            |               2            | 1    |[2,3,1]    |                 |             |                           |         |         |      |                | 
|      |            |               3            | 2    |[2,3,1,2]  |                 |             |                           |         |         |      |                | 
|      |            |               4            | 1    |[2,3,1,2,1]|                 |             |                           |         |         |      |                | 
|      |            |               5            |escape|  escape   |   [1,1,2,2,3]   |      1      |     8 >= 1 --> True       |8 - 1 = 7|    1    |  1   |                |
|      |            |                            |      |           |                 |      1      |     7 >= 1 --> True       |7 - 1 = 6|    2    |  2   |                |
|      |            |                            |      |           |                 |      2      |     6 >= 2 --> True       |6 - 2 = 4|    3    |  3   |                |
|      |            |                            |      |           |                 |      2      |     4 >= 2 --> True       |4 - 2 = 2|    4    |  4   |                | 
|      |            |                            |      |           |                 |      3      |     2 >= 3 --> False      | escape  |  escape |escape|        4       | 
| end  |    end     |           end              | end  |   end     |       end       |     end     |         end               |  end    |    end  |  end |       end      |
'''
# FLOWCHART
# PHOTO IN THE SAME DIRECTORY