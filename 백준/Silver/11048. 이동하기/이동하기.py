import copy
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
candy = list()
for _ in range(n):
    candy.append(list(map(int, input().split())))

dx = [1, 0, 1]
dy = [0, 1, 1]
ans = copy.deepcopy(candy)

for x in range(n):
    for y in range(m):
        for i in range(3):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m:
                nx, ny = x + dx[i], y + dy[i]
                ans[nx][ny] = max(ans[nx][ny], ans[x][y] + candy[nx][ny])

print(ans[n - 1][m - 1])
