
#Test Case 1: What if we put time more than 100000. TESTED: NO ERRORS
#Test Case 2: What if we put time less than 0. TESTED: It will just return 0. 
#Test Case 3: What if we put the number of chores less than 0. TESTED: IT WILL GIVE US AN INDEXERROR: 
#             LIST INDEX OUT OF RANGE
#Test Case 4: What if we put the number of chores more than 100. TESTED: CALCULATES THE NUMBER OF CHORES 
#             YOU CAN DO WITH OVER 100 CHORES.
#Test Case 5: What is the numbers inputed are floats like 15.5 hours. TESTED: VALUEERROR: INVALID LITERAL 
#             FOR INT() WITH BASE 10: '15.5'. THIS IS FIXED BY TAKING ALL THE HOURS VALUES USING FLOAT.
#Test Case 6: What if we take number of hours using negative floats. TESTED: REALISED THAT IF WE PUT 
#             NEGATIVE TIME AND THEN WE PUT NEGATIVE TIME WITH THE TIME THAT WE NEED TO FINISH A CHORE 
#             IT WILL ADD THE VALUE. THIS CAN BE FIXED BY LIMITING THAT WE CANNOT PUT NEGATIVE VALUES BY 
#             RETURNING -1 WHEN NEGATIVE VALUE OF TIME IS INSERTED.
#Test Case 7: If we put the value of time positive and then we put the value of the time we need to do 
#             a chore negative that it will make the time we have availiable bigger. TESTED: IT MADE 
#             THE AVAILABLE BIGGER, WHICH I FIXED BY ADDING A IF STATEMENT TO CHECK IF THE NUMBER THAT 
#             WE NEED TO FINISH A CHORE IS >= 0 IF IT IS TRUE THEN IT WILL APPEND TO THE LIST AND IF IT 
#             IS FALSE, IT WOULD NOT APPEND TO THE LIST.
#Test Case 8: What if we don't put any value. TESTED: It'll return Value error Could not convert 
#             string to float.



def calculateNumberOfChores():

    time = float(input())
    num_chores = int(input())
    if time < 0:
        return -1
    if num_chores < 0:
        return -1

    time_lst = []

    for i in range(num_chores):
        x = float(input())
        if x >= 0:
            time_lst.append(x)

    time_lst.sort()
    
    counter = 0
    i = 0

    while time >= time_lst[i]:
        time = time - time_lst[i]
        counter = counter + 1
        i = i + 1

    print(counter)

calculateNumberOfChores()