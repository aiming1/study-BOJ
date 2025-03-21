import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = deque()
for _ in range(n):
    board.append(str(input())[:-1])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(start):
    global visited
    queue = deque([start])
    color = board[start[0]][start[1]]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
                nx, ny = x + dx[i], y + dy[i]
                if not visited[nx][ny] and board[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append([nx, ny])


ans1 = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            ans1 += 1
            bfs([i, j])

for _ in range(n):
    board.append(board.popleft().replace('G', 'R'))
ans2 = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            ans2 += 1
            bfs([i, j])

print(ans1, ans2)
