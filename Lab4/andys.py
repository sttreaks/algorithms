import string


def add(e):
    return e + '\n'


def s(e, l):
    l += e.split()


'''f = open('input.txt', 'r')
ls = f.readlines()'''
s = input()
ls = s.split('/n')
lis = []
all_let = list(string.ascii_letters)
for i in range(len(ls)):
    lis.append(ls[i].split(' '))
lis = lis[0]
all_let = list(string.ascii_letters)
print(ls)
print(lis)
for i in range(len(lis)):
    lis[i] = lis[i].lower()
for i in range(len(lis)):
    for j in lis(i):
        if j not in all_let:
            i = i.replace(j, '')
new = list(set(lis[0]))
new.sort()
for i in new:
    print(i)
