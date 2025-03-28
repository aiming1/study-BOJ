import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(start, end):
    global board
    sx, sy, ex, ey = start[0], start[1], end[0], end[1]
    queue = deque([(sx, sy, 0)])
    visited = [[False] * w for _ in range(h)]
    visited[sx][sy] = True
    while queue:
        x, y, d = queue.popleft()
        if x == ex and y == ey:
            return d
        for i in range(4):
            if 0 <= x + dx[i] < h and 0 <= y + dy[i] < w:
                nx, ny = x + dx[i], y + dy[i]
                if not visited[nx][ny] and board[nx][ny] != 'x':
                    visited[nx][ny] = True
                    queue.append([nx, ny, d + 1])
    return -1


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = list()
    dirts = list()
    for i in range(h):
        board.append(str(input())[:-1])
        for j in range(w):
            if board[-1][j] == 'o':
                start = [i, j]
            elif board[-1][j] == '*':
                dirts.append([i, j])

    dists = [[0] * len(dirts) for _ in range(len(dirts) + 1)]
    no_ans = False
    for i in range(len(dirts)):
        d = bfs(start, dirts[i])
        if d == -1:
            no_ans = True
            break
        dists[-1][i] = d
        for j in range(i + 1, len(dirts)):
            d = bfs(dirts[i], dirts[j])
            if d == -1:
                no_ans = True
                break
            dists[i][j], dists[j][i] = d, d

    if no_ans:
        print(-1)
    else:
        ans = list()
        for seq in permutations(range(len(dirts))):
            num = 0
            for i in range(1, len(seq)):
                num += dists[seq[i - 1]][seq[i]]
            ans.append(num + dists[-1][seq[0]])
        ans.sort()
        print(ans[0])
