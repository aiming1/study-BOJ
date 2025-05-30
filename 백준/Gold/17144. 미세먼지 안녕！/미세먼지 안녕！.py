import sys

input = sys.stdin.readline

r, c, t = map(int, input().split())
a, cleaner = list(), list()
for _ in range(r):
    a.append(list(map(int, input().split())))
for i in range(r):
    for j in range(c):
        if a[i][j] == -1:
            cleaner.append([i, j])
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def dirt():
    new_board = [[0] * c for _ in range(r)]
    for x, y in cleaner:
        new_board[x][y] = -1
    for i in range(r):
        for j in range(c):
            if a[i][j] > 0:
                chk = 0
                for dx, dy in dir:
                    if 0 <= i + dx < r and 0 <= j + dy < c:
                        if a[i + dx][j + dy] != -1:
                            chk += 1
                            new_board[i + dx][j + dy] += a[i][j] // 5
                new_board[i][j] += (a[i][j] - (a[i][j] // 5) * chk)
    return new_board


def clean():
    new_board = list()
    x1, y1, x2, y2 = cleaner[0][0], cleaner[0][1], cleaner[1][0], cleaner[1][1]
    new_board.append(a[0][1:] + [a[1][-1]])
    for i in range(1, x1):
        new_board.append([a[i - 1][0]] + a[i][1:-1] + [a[i + 1][-1]])
    new_board.append([-1, 0] + a[x1][1:-1])
    new_board.append([-1, 0] + a[x2][1:-1])
    for i in range(x2 + 1, r - 1):
        new_board.append([a[i + 1][0]] + a[i][1:-1] + [a[i - 1][-1]])
    new_board.append(a[-1][1:] + [a[-2][-1]])
    return new_board


for _ in range(t):
    a = dirt()
    a = clean()

ans = 2
for line in a:
    ans += sum(line)
print(ans)
