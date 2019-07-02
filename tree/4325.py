class Tree:
    def __init__(self):
        self.tree = {0: {'children': [], 'father': None, 'level': 0, 'info': []}}
        self.current = 0
        self.way_y = []
        self.way_x = []

    def addLeftChild(self, x):
        self.current += 1
        self.tree.update(
            {self.current: {'children': [], 'father': x,
                            'level': self.tree[x]['level'] + 1, 'info': []}}
        )
        self.tree[x]['children'] = [self.current] + self.tree[x]['children']

    def addRightChild(self, x):
        self.current += 1
        self.tree.update(
            {self.current: {'children': [], 'father': x,
                            'level': self.tree[x]['level'] + 1, 'info': []}}
        )
        self.tree[x]['children'] = self.tree[x]['children'] + [self.current]

    def find(self, x, y):
        for index in range(len(self.tree[x]['children'])):
            if self.tree[x]['children'][index] == y:
                return index
        return -1

    def addRightOf(self, x, y):
        self.current += 1
        division_point = self.find(x, y)
        self.tree.update(
            {self.current: {'children': [], 'father': x,
                            'level': self.tree[x]['level'] + 1, 'info': []}}
        )
        self.tree[x]['children'] = self.tree[x]['children'][:division_point + 1] + [self.current] + \
                                   self.tree[x]['children'][division_point + 1:]

    def delItem(self, x):
        f = self.tree[x]['father']
        division_point = self.find(f, x)
        self.tree[f]['children'] = self.tree[f]['children'][:division_point] + \
                                   self.tree[f]['children'][division_point + 1:]
        del self.tree[x]

    def way(self, x, y):
        if not(self.way_y or self.way_x):
            self.way_x = [x]
            self.way_y = [y]
        if self.way_x[len(self.way_x) - 1] == self.way_y[len(self.way_y) - 1]:
            a = [self.way_x[len(self.way_x) - 1], self.way_x[len(self.way_x) - 2], self.way_y[len(self.way_y) - 2]]
            del self.way_x[len(self.way_x) - 1]
            buff = [self.way_x,  self.way_y[::-1]]
            self.way_x = []
            self.way_y = []
            return [buff, a]
        if self.tree[self.way_x[len(self.way_x) - 1]]['level'] < self.tree[self.way_y[len(self.way_y) - 1]]['level']:
            self.way_y.append(self.tree[self.way_y[len(self.way_y) - 1]]['father'])
        elif self.tree[self.way_x[len(self.way_x) - 1]]['level'] > self.tree[self.way_y[len(self.way_y) - 1]]['level']:
            self.way_x.append(self.tree[self.way_x[len(self.way_x) - 1]]['father'])
        else:
            self.way_y.append(self.tree[self.way_y[len(self.way_y) - 1]]['father'])
            self.way_x.append(self.tree[self.way_x[len(self.way_x) - 1]]['father'])
        return self.way(x, y)

    def underWay(self, x, y):
        def q(_queue):
            _items_under_the_way = 0
            while _queue:
                _items_under_the_way += 1
                for child in self.tree[_queue[0]]['children']:
                    _queue.append(child)
                del _queue[0]
            return _items_under_the_way

        items_under_the_way = 0
        buff = self.way(x, y)
        a = [self.find(buff[1][0], buff[1][1]), self.find(buff[1][0], buff[1][2])]
        a.sort()
        queue = self.tree[buff[1][0]]['children'][a[0]+1:a[1]]
        items_under_the_way += q(queue)
        for index in range(1, len(buff[0][0])):
            queue = self.tree[buff[0][0][index]]['children'][self.find(buff[0][0][index], buff[0][0][index - 1]) + 1:]
            items_under_the_way += q(queue)

        for index in range(1, len(buff[0][1]) - 1):
            queue = self.tree[buff[0][1][index]]['children'][:self.find(buff[0][1][index], buff[0][1][index + 1])]
            items_under_the_way += q(queue)

        return items_under_the_way


if __name__ == "__main__":
    t = Tree()
    n = int(input(''))
    for i in range(n):
        s = input().split(' ')
        if s[0] == 'l':
            t.addLeftChild(int(s[1]))
        elif s[0] == 'r':
            t.addRightChild(int(s[1]))
        elif s[0] == 'a':
            t.addRightOf(int(s[1]), int(s[2]))
        elif s[0] == 'd':
            t.delItem(int(s[1]))
        elif s[0] == 'p':
            w = t.way(int(s[1]), int(s[2]))[0]
            print(len(w[0] + w[1]))
        elif s[0] == 'q':
            print(t.underWay(int(s[1]), int(s[2])))
