f = open('input.txt', 'r')
l = []
k = 0
for i in f:
    l.append(list(map(lambda x: int(x), i.split())))
    if len(l) == 1:
        k = l[0][len(l[0]) - 1]
del l[0]
f.close()

sums = [l[0][0]]
indexes = [(0, 0)]
for i in range(len(l) + len(l[0]) - 2):
    hs = []
    hi = []
    for index in range(len(sums)):
        if indexes[index][0] != len(l) - 1:
            hi.append((indexes[index][0] + 1, indexes[index][1]))
            hs.append(sums[index] + l[indexes[index][0] + 1][indexes[index][1]])
        if indexes[index][1] != len(l[0]) - 1:
            hi.append((indexes[index][0], indexes[index][1] + 1))
            hs.append(sums[index] + l[indexes[index][0]][indexes[index][1] + 1])
    sums = hs
    indexes = hi
del l
del indexes
f = open('output.txt', 'w')
m = max(sums)
print(m, file=f)
h = []
for i in sums:
    if i >= m - k:
        h.append(i)
print(len(h), file=f)
f.close()
