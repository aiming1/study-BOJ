import sys

input = sys.stdin.readline

board = list()
for _ in range(5):
    board.append(input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = set()

def dfs(obj, x, y):
    global ans

    if len(obj) == 6:
        ans.add(obj)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(obj + board[nx][ny], nx, ny)

for i in range(5):
    for j in range(5):
        dfs('', i, j)
print(len(ans))
