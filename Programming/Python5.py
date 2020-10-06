'''
a = None znaci da a nema vrednost i idalje ceka da se pripise vrednost.
'''
a = None
b = None
c = None
d = None
'''
Python uzima inpute u stringovima i onda moras da dodas ispred inputa gde uzimas broj int() da bi se taj input prebacion u
integer.
'''
a = int(input("Enter first number: "))
c = input("Enter: '*' for multiplication '/' for division '+' for addition '-' for subtraction '^' for making first numbert to the power of the second one: ")
b = int(input("Enter second number: "))
'''
Ovo su testovi da vidimo da li smo uzeli dobre brojeve kao i racunske operacije
'''
print("First Number: ", a,";")
print("Second Number: ", b,";")
print("Operation: ", c,";")
'''
Ovo su if, elif, else funkcije kojr pomazu kompjuteru da odabere sta zeli da uradi.
'''
if c == "+":
    d = a + b
    print(d)

elif c == "-":
    d = a - b
    print(d)

elif c == "*":
    d = a * b
    print(d)

elif c == "/":
    d = a / b
    print(d)

elif c == "^":
    d = a ** b
    print(d)

else:
    print("You did not put a valid number!")