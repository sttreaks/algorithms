class Tree:
    def __init__(self, base):
        self.tree = {base: {'children': [], 'father': None, 'level': 0, 'info': []}}
        self.current = 0
        self.way_y = []
        self.way_x = []

    def addRightChild(self, x, cur):
        # self.current += 1
        self.tree.update(
            {cur: {'children': [], 'father': x,
                            'level': self.tree[x]['level'] + 1, 'info': []}}
        )
        self.tree[x]['children'] = self.tree[x]['children'] + [cur]

    def find(self, x, y):
        for index in range(len(self.tree[x]['children'])):
            if self.tree[x]['children'][index] == y:
                return index
        return -1

    def wayDeep(self, x):
        pass

    def findLevel1(self, i):
        if self.tree[i]['level'] == 1:
            return i
        return self.findLevel1(self.tree[i]['father'])


def find(a, subject):
    buff = []
    i = 0
    while i < len(a):
        if a[i][0] == subject:
            buff.append(a[i][1])
            del a[i]
        elif a[i][1] == subject:
            buff.append(a[i][0])
            del a[i]
        else:
            i += 1
    return a, buff


if __name__ == "__main__":
    s = input().split()
    n, k = int(s[0]), int(s[1])
    airports = []
    for i in range(n - 1):
        airports.append(list(map(lambda x: int(x), input().split())))
    airways = Tree(k)
    ch = [k]
    deadlocks = []
    buff = []
    win = []
    while airports or buff:
        buff = []
        for i in ch:
            cur = []
            airports, cur = find(airports, i)
            for j in cur:
                airways.addRightChild(i, j)
            if len(cur) == 0:
                deadlocks.append(i)
            buff += cur
        ch = buff
    del airports
    for i in deadlocks:
        if airways.tree[i]['level'] % 2 == 1:
            win.append(airways.findLevel1(i))
    if win:
        print('First player wins flying to airport {}'.format(min(win)))
    else:
        print('First player loses')
