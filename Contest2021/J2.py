number = int(input())
names = []
bids = []
for i in range(number):
    name = input()
    names.append(name)
    bid = input()
    bids.append(bid)
a = bids[0]
for i in range(1, len(bids), 1):
    if bids[i] > a:
        a = bids[i]
b = bids.index(a)
print(names[b])
