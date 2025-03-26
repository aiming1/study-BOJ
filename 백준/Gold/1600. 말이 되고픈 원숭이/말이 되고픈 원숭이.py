import sys
from collections import deque

input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
board = list()
for _ in range(h):
    board.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
hdx = [-2, -2, -1, -1, 1, 1, 2, 2]
hdy = [-1, 1, -2, 2, -2, 2, -1, 1]
visited = [[[0] * w for _ in range(h)] for _ in range(k + 1)]


def bfs():
    queue = deque([(0, 0, k)])
    while queue:
        x, y, c = queue.popleft()
        if x == h - 1 and y == w - 1:
            return visited[c][x][y]
        if c > 0:  # 말처럼 이동할 수 있는 횟수가 남아 있음
            for i in range(8):
                nx, ny = x + hdx[i], y + hdy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if board[nx][ny] != 1 and visited[c - 1][nx][ny] == 0:
                        visited[c - 1][nx][ny] = visited[c][x][y] + 1
                        queue.append([nx, ny, c - 1])
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] != 1 and visited[c][nx][ny] == 0:
                    visited[c][nx][ny] = visited[c][x][y] + 1
                    queue.append([nx, ny, c])
    return -1


print(bfs())
