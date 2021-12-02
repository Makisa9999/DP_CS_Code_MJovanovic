# Try exept works like this
    # try: 
        # Ececute this code
    # except: 
        # If the try code fails, then execute this code
def findSumLSTB(lst):
    sum=0
    for i in range(len(lst)):
        try:
            temp = float(lst[i])
            sum = sum + temp
            #sum = sum + float(lst[i])
        except:
            pass

def dogAge1():
    print("Dog Age Calculator")

    while True:
        try: 
            age = input("What is your age: ")
            age = int(age)
            break
        except: 
            print("Please input an integer value")

    dogAge  = age * 7

    return "You are",dogAge,"years old."

def catAge1():
    print("Cat Age Calculator")

    age = input("What is your age: ")

    if age.isnumeric():
        catAge = int(age) * 6
        pass
    else: 
        print("Please input a valid integer!")

    return "You are", catAge, "years old."

print(catAge1())