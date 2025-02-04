import sys

input = sys.stdin.readline

n, m = map(int, input().split())
square = [[0] * (m + 2)]
for _ in range(n):
    square.append([0] + list(map(int, input().split())) + [0])
square.append([0] * (m + 2))

''' 밑면, 윗면 '''
ans = n * m * 2

''' 동쪽, 서쪽 '''
for i in range(1, n + 1):
    for j in range(m, 0, -1):
        if square[i][j] > square[i][j + 1]:
            ans = ans + square[i][j] - square[i][j + 1]
    for j in range(1, m + 1):
        if square[i][j] > square[i][j - 1]:
            ans = ans + square[i][j] - square[i][j - 1]


''' 남쪽, 북쪽 '''
for j in range(1, m + 1):
    for i in range(n, 0, -1):
        if square[i][j] > square[i + 1][j]:
            ans = ans + square[i][j] - square[i + 1][j]
    for i in range(1, n + 1):
        if square[i][j] > square[i - 1][j]:
            ans = ans + square[i][j] - square[i - 1][j]

print(ans)
