import copy
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
visited_ori = [[False] * n for _ in range(n)]
virus = list()
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            visited_ori[i][j] = True
        elif line[j] == 2:
            virus.append([i, j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(start, visited):
    queue = deque()
    for i, j in start:
        visited[i][j] = True
        queue.append([i, j, 0])
    while queue:
        x, y, dis = queue.popleft()
        for i in range(4):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
                nx, ny = x + dx[i], y + dy[i]
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny, dis + 1])
    return visited, dis


def check_visited(visited):
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                return False
    return True


ans = -1
for t in combinations(virus, m):
    new_visited, dist = bfs(t, copy.deepcopy(visited_ori))
    if check_visited(new_visited):
        ans = min(ans, dist) if ans != -1 else dist

print(ans)
