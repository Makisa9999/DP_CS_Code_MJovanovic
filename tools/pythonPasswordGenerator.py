import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCEDFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"

all = lower + upper + numbers
lenght = 16
password = "".join(random.sample(all,lenght))
print("........................................................................")
print(password)
print("........................................................................")