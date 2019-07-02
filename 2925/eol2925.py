def find(samp):
    s = ''
    try:
        if samp[samp['way'][0]][0] == samp[samp['way'][1]][0]:
            s += samp[samp['way'][0]][1]
            s += ' '
            s += samp[samp['way'][0]][0]
            s += ' '
        elif samp[samp['way'][0]][0] == samp[samp['way'][1]][1]:
            s += samp[samp['way'][0]][1]
            s += ' '
            s += samp[samp['way'][0]][0]
            s += ' '
        elif samp[samp['way'][0]][1] == samp[samp['way'][1]][1]:
            s += samp[samp['way'][0]][0]
            s += ' '
            s += samp[samp['way'][0]][1]
            s += ' '
        elif samp[samp['way'][0]][1] == samp[samp['way'][1]][0]:
            s += samp[samp['way'][0]][0]
            s += ' '
            s += samp[samp['way'][0]][1]
            s += ' '
        else:
            return [False, s]
        for indx in range(1, len(samp['way'])):
            if s[len(s) - 2] == samp[samp['way'][indx]][0]:
                s += samp[samp['way'][indx]][1]
                s += ' '
                if indx == len(samp['way']) - 1:
                    s += samp[samp['way'][indx]][1]
                    s += ' '
            elif s[len(s) - 2] == samp[samp['way'][indx]][1]:
                s += samp[samp['way'][indx]][0]
                s += ' '
                if indx == len(samp['way']) - 1:
                    s += samp[samp['way'][indx]][0]
                    s += ' '
            else:
                return [False, s]
        s = s[:len(s) - 2]
        return [True, s]
    except KeyError:
        return [False, s]


out = open('output.txt', 'w')
f = open('input.txt', 'r')
buff = {}
c = 0
first = False
way = True
for i in f:
    if i.count('Sample') == 1:
        c += 1
        buff.update({c: {}})
        if first:
            print('Sample {}'.format(c - 1), file=out)
            w = find(buff[c - 1])
            if w[0]:
                b = w[1][0] + ' ' + w[1][len(w[1]) - 2]
                print('YES', file=out)
                print(b, file=out)
                print('', file=out)
            else:
                print('NO', file=out)
                print('', file=out)
        first = True
        way = True
    else:
        i = i.replace('\n', '')
        k = i.split()
        if way and len(k) == 1:
            buff[c].update({'way': i})
            way = False
        elif len(k) == 1:
            buff[c].update({'max': int(i)})
        elif len(k) == 3:
            buff[c].update({k[2]: (k[0], k[1])})

print('Sample {}'.format(c), file=out)
w = find(buff[c])
if w[0]:
    b = w[1][0] + ' ' + w[1][len(w[1]) - 2]
    print('YES', file=out)
    print(b, file=out)
    print('', file=out)
else:
    print('NO', file=out)
    print('', file=out)
out.close()
f.close()
