s = input().split(' ')
v_max, eat_time = int(s[0]), int(s[1])
n = int(input())
flowers = []
for i in range(n):
    s = input().split(' ')
    flowers.append([s[0], s[1].split(':')])
print(flowers)



time += distance/v_max
print(time)
out = open('output2.txt', 'w')
time = str(round(time//60)) + ':' + str(round(time % 60))
print(time)
out.write(time)
