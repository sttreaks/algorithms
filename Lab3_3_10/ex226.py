f = open('input.txt', 'r')
ls = f.readlines()
f.close()
f = open('output.txt', 'w')
for i in range(len(ls)):
    ls[i] = ls[i].replace('\n', '')
    ls[i] = ls[i].split(' ')
for i in range(int(ls[0][0])):
    if ls[2][0] == ls[1][i]:
        f.write(str(i) + ' ')
