import copy
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
board = list()
virus = list()
empty_space = 0
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] == 2:
            virus.append([i, j])
        elif board[i][j] == 0:
            empty_space += 1
if empty_space == 0:
    print(0)
    exit()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

''' 0: 빈 칸  1: 벽  2: 비활성 바이러스  3: 활성 바이러스 '''
def bfs(start):
    queue = deque()
    visited = [[False] * n for _ in range(n)]
    this_empty = empty_space
    for x, y in start:
        queue.append([x, y, 0])
        visited[x][y] = True
    while queue:
        x, y, t = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] != 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny, t + 1])
                    if board[nx][ny] == 0:
                        this_empty -= 1
        if this_empty == 0:
            return t + 1
    return -1


ans = set()
for vc in combinations(virus, m):
    ans.add(bfs(vc))
ans -= {-1}
ans = list(ans)
print(min(ans) if len(ans) else -1)
