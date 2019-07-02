import math

def input_():
    s = input().split(' ')
    v_max, eat_time = int(s[0]), int(s[1])
    n = int(input())
    flowers = []
    x1 = 0
    for i in range(n):
        s = input().split(' ')
        h = s[1].split(':')
        flowers.append([int(s[0]) - x1, int(h[0])*60 + int(h[1])])
        x1 = int(s[0])
    return v_max, eat_time, flowers, x1


def output(time):
    time = int(math.ceil(time))
    if len(str(time // 60)) == 1:
        if len(str(time % 60)) == 1:
            print('0' + str(time // 60) + ':0' + str(time % 60))
        else:
            print('0' + str(time // 60) + ':' + str(time % 60))
    else:
        if len(str(time % 60)) == 1:
            print(str(time // 60) + ':0' + str(time % 60))
        else:
            print(time // 60) + ':' + str(time % 60)




if __name__ == "__main__":
    time = 0
    k = 0
    v_max, eat_time, flowers, full_d = input_()
    if eat_time == 0:
        if flowers[len(flowers) - 1][1] > full_d / v_max:
            time = flowers[len(flowers) - 1][1] + full_d / v_max
        else:
            time = 2 * full_d / v_max
        output(time)
    else:
        if flowers[len(flowers) - 1][1] <= full_d / v_max:
            time = 2*full_d / v_max + eat_time * len(flowers)
        elif not flowers:
            pass
