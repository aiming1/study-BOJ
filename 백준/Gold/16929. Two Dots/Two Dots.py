import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = list()
for _ in range(n):
    board.append(str(input())[:-1])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * m for _ in range(n)]
visited_board = [[False] * m for _ in range(n)]


def dfs(color, x, y, past_dir):
    global visited

    for i in range(4):
        if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m:
            xx, yy = x + dx[i], y + dy[i]
            if board[xx][yy] == color:
                if visited[xx][yy] and i != past_dir:
                    print("Yes")
                    exit()
                if not visited[xx][yy]:
                    visited[xx][yy], visited_board[xx][yy] = True, True
                    dfs(color, xx, yy, (i + 2) % 4)
                    visited[xx][yy] = False


for i in range(n):
    for j in range(m):
        if visited_board[i][j]:
            continue

        visited[i][j], visited_board[i][j] = True, True
        dfs(board[i][j], i, j, -1)

print("No")
