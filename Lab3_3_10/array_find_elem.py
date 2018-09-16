f = open('input.txt', 'r')
ls = f.readlines()
out = open('output.txt', 'w')
for i in range(len(ls)):
    ls[i] = ls[i].replace('\n', '')
    ls[i] = ls[i].split(' ')
for i in range(int(ls[0][0])):
    ls[1][i] = int(ls[1][i])
    if ls[1][i] == int(ls[2][0]):
        out.write(str(i+1) + ' ')             # НЕ ЗНАЮ НУЖНЫ ЛИ ИНДЕКСЫ ЭЛЕМЕНТОВ ИЛИ НОМЕРА ПОЭТОМУ НАПИСАЛ +1
print(ls)
