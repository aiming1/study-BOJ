import sys
from collections import deque

input = sys.stdin.readline


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    global visited
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
    return 1


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    visited = [[True] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        visited[b][a] = False

    ans = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                ans += bfs(i, j)
    print(ans)
