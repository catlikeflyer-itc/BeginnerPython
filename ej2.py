count = {}
f = open('fruits.txt', 'r')
flist = f.read().split()
for word in flist:
    if word not in count.keys():
        count[word] = 1
    elif word in count.keys():
        count[word] += 1
print(count)
