n, s, e = list(map(lambda x: int(x), input().split()))
s -= 1
e -= 1
gr = {}
for i in range(n):
    gr.update({i: {0: [], 1: [], 2: []}})

for j in range(2):
    m = int(input())
    for i in range(m):
        pointA, pointB, lenght = list(map(lambda x: int(x), input().split()))
        gr[pointA - 1][j].append([pointB - 1, lenght])
        gr[pointB - 1][j].append([pointA - 1, lenght])

buff = [s]
res = False
c = 0
gr[s][2] = 0
while buff:
    cur = buff[0]
    buff = buff[1:]
    for j in gr[cur][gr[cur][2]]:
        if gr[j[0]][2] == gr[cur][2]:
            buff = []
            res = cur
            break
        else:
            if gr[cur][2] == 0:
                gr[j[0]][2] = 1
            else:
                gr[j[0]][2] = 0
            buff.append(j[0])
            c += 1
        if c == n * 5:
            buff = []
            break
if res:
    print(-1)
else:
    pass