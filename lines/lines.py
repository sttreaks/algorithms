def printWay(lines):
    for line in lines:
        buff = ""
        for sym in line:
            buff += sym
        print(buff)


n = int(input())
l = []
x, y = -1, -1
xe, ye = -1, -1
for i in range(n):
    buff = []
    k = input()
    if x == -1:
        y, x = i, k.find('@')
    if xe == -1:
        ye, xe = i, k.find('X')
    for j in k:
        buff.append(j)
    l.append(buff)

hl = [[-1 for i in range(n)] for j in range(n)]
hl[y][x] = 1
indexes = [[y, x]]
way = False
for i in range(n*n + 1):
    buff = []
    for j in indexes:
        if 0 <= j[1] + 1 < n and \
                l[j[0]][j[1] + 1] in '.X'\
                and hl[j[0]][j[1] + 1] == -1:
            hl[j[0]][j[1] + 1] = hl[j[0]][j[1]] + 1
            buff.append([j[0], j[1] + 1])
        if 0 <= j[1] - 1 < n and \
                l[j[0]][j[1] - 1] in '.X'\
                and hl[j[0]][j[1] - 1] == -1:
            hl[j[0]][j[1] - 1] = hl[j[0]][j[1]] + 1
            buff.append([j[0], j[1] - 1])
        if 0 <= j[0] + 1 < n and \
                l[j[0] + 1][j[1]] in '.X'\
                and hl[j[0] + 1][j[1]] == -1:
            hl[j[0] + 1][j[1]] = hl[j[0]][j[1]] + 1
            buff.append([j[0] + 1, j[1]])
        if 0 <= j[0] - 1 < n and \
                l[j[0] - 1][j[1]] in '.X'\
                and hl[j[0] - 1][j[1]] == -1:
            hl[j[0] - 1][j[1]] = hl[j[0]][j[1]] + 1
            buff.append([j[0] - 1, j[1]])
        if j == [ye, xe]:
            way = True
            break
    indexes = buff
    if way:
        break
if way:
    print('Y')
    indexes = [[ye, xe]]
    way = False
    c = hl[ye][xe]
    l[ye][xe] = '+'
    for i in range(n * n + 1):
        buff = []
        for j in indexes:
            if 0 <= j[1] + 1 < n and hl[j[0]][j[1] + 1] == c - 1:
                c -= 1
                l[j[0]][j[1] + 1] = '+'
                buff.append([j[0], j[1] + 1])
            elif 0 <= j[1] - 1 < n and hl[j[0]][j[1] - 1] == c - 1:
                c -= 1
                l[j[0]][j[1] - 1] = '+'
                buff.append([j[0], j[1] - 1])
            elif 0 <= j[0] + 1 < n and hl[j[0] + 1][j[1]] == c - 1:
                c -= 1
                l[j[0] + 1][j[1]] = '+'
                buff.append([j[0] + 1, j[1]])
            elif 0 <= j[0] - 1 < n and hl[j[0] - 1][j[1]] == c - 1:
                c -= 1
                l[j[0] - 1][j[1]] = '+'
                buff.append([j[0] - 1, j[1]])
            elif j == [y, x]:
                way = True
                break
        indexes = buff
        if way:
            break
    printWay(l)
else:
    print('N')
