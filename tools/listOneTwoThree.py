one = ["Juice", "Hand", "Lamp", "Car", "Cat"]
two = ["Bowl", "Alarm", "Shirt", "Book", "Apple"]
three = []
for i in range(0, len(one), 1):
    
    three = three + [one[i]] + [two[i]]
print(three)
    