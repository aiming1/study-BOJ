import copy
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = list()
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(sx, sy):
    global ans
    next_queue = deque([(sx, sy, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[sx][sy] = True
    while next_queue:
        queue = copy.deepcopy(next_queue)
        next_queue.clear()
        while queue:
            x, y, d = queue.popleft()
            for i in range(8):
                if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m:
                    nx, ny = x + dx[i], y + dy[i]
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        if board[nx][ny] == 0:
                            if ans[nx * m + ny] == 0:
                                ans[nx * m + ny] = d + 1
                            else:
                                ans[nx * m + ny] = min(ans[nx * m + ny], d + 1)
                        next_queue.append([nx, ny, d + 1])


ans = [0] * (m * n)
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            bfs(i, j)

print(max(ans))
