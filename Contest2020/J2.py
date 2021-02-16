day = 0
target = int(input())
initial = int(input())
spread = int(input())
total_infected = initial

if initial == target:
    print(1)
else:
    while total_infected <= target:
        day += 1
        total_infected += ((spread ** day) * initial)
    print(day)