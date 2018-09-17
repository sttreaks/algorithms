f = open('input2.txt', 'r')
ls = f.readlines()
for i in range(len(ls)):
    ls[i] = ls[i].replace('\n', '')
    ls[i] = ls[i].split(' ')

v_max = int(ls[0][0])
eat_time = int(ls[0][1])
n = int(ls[1][0])
flow = ls[2:(2+n)]

time = 0
distance = 0
for i in range(n):
    flower_d = int(flow[i][0]) - distance
    time_get = (flower_d - distance)/v_max
    buff = flow[i][1].split(':')
    if time_get > (int(buff[0])*60 + int(buff[1])):
        distance += flower_d
        time += flower_d / v_max  + eat_time
    else:
        distance += flower_d
        time += int(buff[0])*60 + int(buff[1]) + eat_time

time += distance/v_max
print(time)
out = open('output2.txt', 'w')
time = str(round(time//60)) + ':' + str(round(time % 60))
print(time)
out.write(time)
