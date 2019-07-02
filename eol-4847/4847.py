def check(dict, el):
    for key in dict.keys():
        if dict[key].get(el) is not None:
            del q[key][el]
            return True
    return None


q = {}
cmnd = []
f = open('input.txt', 'r')
it = 0
for i in f:
    cmnd.append(i.split(' '))
    # print(cmnd)
    if len(cmnd[it]) >= 3:
        cmnd[it][2] = int(cmnd[it][2])
    else:
        cmnd[it] = ['POP']
    it += 1
f.close()
f = open('output.txt', 'w')
for i in cmnd:
    # print(i)
    if i[0] == 'ADD':
        if q.get(i[2]) is None:
            q.update({i[2]: {i[1]: i[2]}})
        else:
            q[i[2]].update({i[1]: i[2]})
    elif i[0] == 'POP':
        p = None
        print(q)
        while True:
            k = q.keys()
            m = 0
            for j in k:
                if j > m and q[j] is not None:
                    m = j
            print(m)
            if q[m] == {}:
                del q[m]
            else:
                p = q[m].popitem()
                print(p[0], p[1], file=f)
                if q[m] == {}:
                    del q[m]
                break
    elif i[0] == 'CHANGE':
        check(q, i[1])
        if q.get(i[2]) is None:
            q.update({i[2]: {i[1]: i[2]}})
        else:
            q[i[2]].update({i[1]: i[2]})
    # print(q)
f.close()
