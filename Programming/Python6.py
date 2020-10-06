'''
#This is where computer will start counting 100 numbers starting aat 0 and ending at 99
for i in range(100):
    print(i)

#Here I made a input so I can tell python where to start counting. I input some value and python will start counting from zero
#to that value. print(i + 1) Tells computer not to start from 0 but to start from 1 because it is adding one value each time.
#Here also because python takes inputs as strings, where is the input you can see that I put it in the int(input) this will
#change that input to an integer so computer will have a number stored. 

count = int(input("How far do you want me to count to? "))
for i in range(count):
    print(i + 1)

print("end")


Here the first digit is where you want the computer to start counting. The second digit is where do you want it to finish.
The third value is the step that you want it to make. So in this case you will see that the computer is counting 

for i in range(0, 1000, 5):
    print(i)

for i in range(0, 1000, 1):
    print(i)

str = ""
str = input("What is your word?")
l = len(str)

for i in range(0, l, 1):
    print(str)


str = "janjsbjacodemajncode"
dstr = str.replace("code", "")
print(str)
print(dstr)
'''
#This is going to take second item from this list and going to print out
y = int(input("Enter a number between 1 and 4: "))
y = y - 1
x = ["apple", "banana", "cherry", "strawberry"]
print(x[y])