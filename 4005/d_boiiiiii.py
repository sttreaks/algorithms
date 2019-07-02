from collections import deque


def f(deq1, deq2, l):
    for i in range(2*10**5):
        if len(deq1) == 0:
            return "second " + str(i)
        elif len(deq2) == 0:
            return "first " + str(i)
        else:
            p1 = deq1.popleft()
            p2 = deq2.popleft()
            if (p1 > p2 and (p1 != l - 1 or p2 != 0)) or (p1 == 0 and p2 == l - 1):
                deq1.append(p1)
                deq1.append(p2)
            else:
                deq2.append(p1)
                deq2.append(p2)
    return "draw"


d1 = deque()
d2 = deque()
n = int(input())
s1 = input().split(' ')
s2 = input().split(' ')
for char in range(len(s1)):
    d1.append(int(s1[char]))
    d2.append(int(s2[char]))
print(f(d1, d2, n))
