import sys
from collections import deque
from itertools import product

input = sys.stdin.readline

n, m = map(int, input().split())
board = list()
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def get_dead_stone(white_set):
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2 and not visited[i][j]:
                visited[i][j] = True
                cnt += bfs(i, j, visited, white_set)
    return cnt

def bfs(i, j, visited, white_set):
    queue = deque([(i, j)])
    cnt = 0
    flag = True
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for a in range(4):
            nx, ny = x + dx[a], y + dy[a]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 2 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif board[nx][ny] == 0 and (nx, ny) not in white_set:
                    flag = False
    return cnt if flag else 0

ans = set()
for x1, x2, y1, y2 in product(range(0, n), range(0, n), range(0, m), range(0, m)):
    if not (x1 == x2 and y1 == y2) and board[x1][y1] == 0 and board[x2][y2] == 0:
        ans.add(get_dead_stone({(x1, y1), (x2, y2)}))

print(max(ans))
