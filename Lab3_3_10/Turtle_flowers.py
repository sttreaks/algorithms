import math


def max_(a, b):
    if a > b:
        return a
    return b


def input_():
    s = input().split(' ')
    v, dt = int(s[0]), int(s[1])
    n = int(input())
    fl = []
    x1 = 0
    for line in range(n):
        s = input().split(' ')
        h = s[1].split(':')
        fl.append([float(s[0]) - x1, float(h[0]) * 60.0 + float(h[1])])
        x1 = float(s[0])
    return v, dt, fl, x1


def output(t):
    if len(str(t // 60)) == 1:
        if len(str(t % 60)) == 1:
            print('0' + str(t // 60) + ':0' + str(t % 60))
        else:
            print('0' + str(t // 60) + ':' + str(t % 60))
    else:
        if len(str(t % 60)) == 1:
            print(str(t // 60) + ':0' + str(t % 60))
        else:
            print(str(t // 60) + ':' + str(t % 60))


if __name__ == "__main__":

    time = 0
    k = 0
    v_max, eat_time, flowers, full_d = input_()
    if eat_time == 0:
        time = max_(full_d / v_max, flowers[len(flowers) - 1][1]) + full_d / v_max
    elif flowers[len(flowers) - 1][1] <= full_d / v_max:
        time = full_d * 2 / v_max + len(flowers) * eat_time
    elif not flowers:
        pass
    else:
        l = 0
        r = flowers[len(flowers) - 1][1]
        mid = None
        k = None
        while r - l > 0.0001:
            mid = l + (r - l) / 2
            time = mid
            k = 0
            for i in range(len(flowers) - 1):
                time += flowers[i][0] / v_max
                if time >= flowers[i][1]:
                    time += eat_time
                    k += 1
            time += flowers[len(flowers) - 1][0] / v_max
            if time == flowers[len(flowers) - 1][1]:
                break
            if time > flowers[len(flowers) - 1][1]:
                r = mid
            else:
                l = mid
        time += eat_time * (len(flowers) - k) + full_d / v_max
    time = int(math.ceil(time))
    output(time)
