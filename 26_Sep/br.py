def check():
    h = []

    return h


n = int(input())
s = 0
zp = []
zp2 = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    s = input().split(' ')
    for j in range(n):
        # noinspection PyTypeChecker
        s[j] = int(s[j])
    zp.append(s)

s = 0
for i in range(n):
    h = []
    for j in range(n):
        h.append(zp[j][i])
    for j in range(n):
        zp2[j][i] = zp[j][i] - min(h)

h = check()
if h is []:
    print(zp2)
    for j in range(n):
        h2 = []
        for i in range(n):
            h2.append(zp[j][i])
        for j in range(n):
            # noinspection PyTypeChecker
            zp2[j][i] = zp2[j][i] - min(h2)
    h = check()
    print(h)
    if h is []:
        pass
    else:
        for i in h:
            s += zp[i[0]][i[1]]
else:
    for i in h:
        s += zp[i[0]][i[1]]
print(zp2)
print(s)
