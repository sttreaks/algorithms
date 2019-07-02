class Graph:
    def __init__(self, n: int):
        self.n = n
        self.g = {n: {'way': None}}
        self.g.update({1: {'way': 0}})

    def addWay(self, u, v, c):
        if self.g.get(u, -1) == -1:
            self.g.update({u: {'way': None}})
        if self.g.get(v, -1) == -1:
            self.g.update({v: {'way': None}})
        if self.g[u].get(v, -1) == -1 or self.g[u].get(v, -1) > c:
            self.g[u].update({v: c})
        if self.g[v]['way'] is None or self.g[v]['way'] > self.g[u]['way'] + c:
            self.g[v]['way'] = self.g[u]['way'] + c

    def get(self):
        return self.g[self.n]['way']


def find(a, subject):
    a1 = a.copy()
    buff = []
    i = 0
    while i < len(a):
        if a[i][0] == subject:
            buff.append([a[i][1], a[i][2]])
            del a[i]
        elif a[i][1] == subject:
            buff.append([a[i][0], a[i][2]])
            del a[i]
        else:
            i += 1
    k = (a1 == a and buff == [])
    return a, buff, k


if __name__ == '__main__':
    n, m = list(map(lambda x: int(x), input().split()))
    g = Graph(n)
    planets = []
    for i in range(m):
        planets.append(list(map(lambda x: int(x), input().split())))
    ch = [[1]]
    q = False
    while planets or ch:
        buff = []
        for i in ch:
            cur = []
            p, cur, k = find(planets, i[0])
            if k:
                q = True
            for j in cur:
                g.addWay(i[0], j[0], j[1])
                g.addWay(j[0], i[0], j[1])
            buff += cur
        if q:
            break
        ch = buff
    if g.get() is None:
        print(-1)
    else:
        print(g.get())
