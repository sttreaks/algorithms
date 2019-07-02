def max(a, b):
    if a > b:
        return a
    return b


def f(a, i, j, value, p):
    value += a[i][j]
    if (i == 0) and (j == 0):
        if p[i][j].find('*') == -1:
            p[i][j] += "*"
        return value
    if i == 0:
        return f(a, i, j - 1, value, p)
    elif j == 0:
        return f(a, i - 1, j, value, p)
    if f(a, i - 1, j, value, p) > f(a, i, j - 1, value, p):
        if p[i - 1][j].find('*') == -1:
            p[i - 1][j] += "*"
        return f(a, i - 1, j, value, p)
    else:
        if p[i][j - 1].find('*') == -1:
            p[i][j - 1] += "*"
        return f(a, i, j - 1, value, p)


def get_max_value(board):
    p = []
    for i in range(len(board)):
        p.append([])
        for j in range(len(board[0])):
            p[i].append(str(board[i][j]))
    unswer = f(board, len(board) - 1, len(board[0]) - 1, 0, p)
    p[len(board) - 1][len(board[0]) - 1] += '*'
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(p[i][j], end=' ')
        print()
    return unswer
