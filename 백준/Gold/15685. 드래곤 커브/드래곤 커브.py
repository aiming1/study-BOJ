import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
curve = []
for _ in range(n):
    curve.append(list(map(int, input().split())))

visited = [[False] * 101 for _ in range(101)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
'''
    0: →     1: ↑      2: ←      3: ↓
'''
for item in curve:
    dir = deque([item[2]])
    for _ in range(item[3]):
        for i in range(len(dir) - 1, -1, -1):
            dir.append((dir[i] + 1) % 4)

    x, y = item[0], item[1]
    visited[x][y] = True
    while dir:
        next_dir = dir.popleft()
        if 0 <= x + dx[next_dir] <= 100 and 0 <= y + dy[next_dir] <= 100:
            x += dx[next_dir]
            y += dy[next_dir]
            visited[x][y] = True

ans = 0
for i in range(100):
    for j in range(100):
        if visited[i][j] and visited[i + 1][j] and visited[i][j + 1] and visited[i + 1][j + 1]:
            ans += 1

print(ans)
