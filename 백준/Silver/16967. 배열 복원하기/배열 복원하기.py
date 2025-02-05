import sys

input = sys.stdin.readline

h, w, x, y = map(int, input().split())
b = []
for _ in range(h + x):
    b.append(list(map(int, input().split())))

''' 위 '''
for i in range(x):
    b[i] = b[i][:w]
    print(*b[i])

''' 중간 '''
if h - x > x:
    for i in range(x, h):
        b[i] = b[i][:y] + [(b[i][j] - b[i - x][j - y]) for j in range(y, w)]
        print(*b[i])

''' 아래 '''
if h - x <= x:
    for i in range(h - x, 0, -1):
        b[-i] = b[-i][y:]
        print(*b[-i])