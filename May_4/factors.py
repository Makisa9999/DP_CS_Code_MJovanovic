# Write a function that takes an integer n and returns a list of all factors. 
def factors(n):
    a = []
    for i in range(1, n+1, 1):
        if n % i == 0:
            a.append(i)
    return a

# print(factors(25012))

# Write a function that will return a list containing the products of all possible 3 digit numbers.  

def possible3DigitNumbers(number):
    lst = []
    for i in range(1, 999, 1):
        multipleOfNumber = number * i
        if multipleOfNumber >= 100 and multipleOfNumber <= 999:
            lst.append(multipleOfNumber)
    return lst
# print(possible3DigitNumbers(5))
# print(possible3DigitNumbers(2))

# Write a function that takes an integer n and returns true if it is a palindrome and false otherwise. 

def palindrome(string):
    reversedString = string[::-1]
    if reversedString == string:
        return True
    return False

# print(palindrome("ana"))

def largePalindrome():
    lstPalindrome = []
    multiplied = []

    for i in range(100, 1000, 1):
        i = str(i)
        if palindrome(i):
            lstPalindrome.append(i)
    for i in range(0, len(lstPalindrome), 1):
        for j in range(i, len(lstPalindrome), 1):
            a = int(lstPalindrome[i]) * int(lstPalindrome[j])
            multiplied.append(a)
    lstPalindrome = []
    for i in range(len(multiplied)):
        if palindrome(str(multiplied[i])):
            lstPalindrome.append(multiplied[i])
            lstPalindrome.sort()
    return lstPalindrome[-1]

print(largePalindrome())