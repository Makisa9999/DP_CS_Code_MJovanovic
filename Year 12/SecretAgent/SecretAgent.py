import random

firstAndLastName = input("What is your first and last name? \n")
firstAndLastName = firstAndLastName.split(" ")

firstName = firstAndLastName[0]
lastName = firstAndLastName[1]

shuffledFirstName = ''.join(random.sample(firstName, len(firstName)))
shuffledLastName = ''.join(random.sample(lastName, len(lastName)))

shuffledFirstName = shuffledFirstName.lower().capitalize()
shuffledLastName = shuffledLastName.lower().capitalize()

print(shuffledFirstName, shuffledLastName)