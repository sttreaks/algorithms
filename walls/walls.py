n = int(input())
l = []
x, y = 0, 0
xe, ye = n-1, n-1
for i in range(n):
    buff = []
    k = input()
    for j in k:
        buff.append(j)
    l.append(buff)

hl = [[-1 for i in range(n)] for j in range(n)]
hl[y][x] = 1
indexes = [[y, x]]
way = False
s = 0
for i in range(n*n + 1):
    buff = []
    for j in indexes:
        if 0 <= j[1] + 1 < n and \
                l[j[0]][j[1] + 1] != '#':
            if hl[j[0]][j[1] + 1] == -1:
                hl[j[0]][j[1] + 1] = hl[j[0]][j[1]] + 1
                buff.append([j[0], j[1] + 1])
        else:
            s += 1
        if 0 <= j[1] - 1 < n and \
                l[j[0]][j[1] - 1] != '#':
            if hl[j[0]][j[1] - 1] == -1:
                hl[j[0]][j[1] - 1] = hl[j[0]][j[1]] + 1
                buff.append([j[0], j[1] - 1])
        else:
            s += 1
        if 0 <= j[0] + 1 < n and \
                l[j[0] + 1][j[1]] != '#':
            if hl[j[0] + 1][j[1]] == -1:
                hl[j[0] + 1][j[1]] = hl[j[0]][j[1]] + 1
                buff.append([j[0] + 1, j[1]])
        else:
            s += 1
        if 0 <= j[0] - 1 < n and \
                l[j[0] - 1][j[1]] != '#':
            if hl[j[0] - 1][j[1]] == -1:
                hl[j[0] - 1][j[1]] = hl[j[0]][j[1]] + 1
                buff.append([j[0] - 1, j[1]])
        else:
            s += 1
        if j == [ye, xe]:
            way = True
            break
    indexes = buff
    if way:
        break
if way:
    print(s)
