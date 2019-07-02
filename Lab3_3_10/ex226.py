n = int(input())
s = input().split(' ')
ls = [int(s[i]) for i in range(n)]
x = int(input())
s = ''
for i in range(n):
    if ls[i] == x:
        print(i)
