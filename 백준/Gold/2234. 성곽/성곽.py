import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = list()
for _ in range(m):
    board.append(list(map(int, input().split())))

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
visited = [[False] * n for _ in range(m)]
group = [[0] * n for _ in range(m)]
group_size = dict()


def bfs(sx, sy, flag):
    global visited
    queue = deque([(sx, sy)])
    v = [[sx, sy]]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            if 0 <= x + dx[i] < m and 0 <= y + dy[i] < n:
                nx, ny = x + dx[i], y + dy[i]
                if not flag and not visited[nx][ny] and board[x][y] & (1 << i) == 0:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                    v.append([nx, ny])
                if flag and not visited[nx][ny] and group[x][y] != group[nx][ny]:
                    return group_size[group[x][y]] + group_size[group[nx][ny]]
    if not flag:
        return v


def make_group(v, num):
    global group, group_size
    for x, y in v:
        group[x][y] = num
    group_size[num] = len(v)
    return num + 1


g_num = 1
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            g = bfs(i, j, False)
            g_num = make_group(g, g_num)

print(len(group_size))
print(max(group_size.values()))

visited = [[False] * n for _ in range(m)]
ans_3 = set()
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            a = bfs(i, j, True)
            if a.__class__ == int:
                ans_3.add(a)
ans_3 = list(ans_3)
ans_3.sort()
print(ans_3[-1])
