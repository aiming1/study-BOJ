import copy
import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().split())
board = list()
for _ in range(n):
    board.append(list(map(int, input().split())))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


''' bfs - 연합 구하기 '''
def bfs(queue):
    global visited
    united = copy.deepcopy(queue)  # 연합에 속하는 국가
    while queue:
        now = queue.popleft()
        x, y = now[0], now[1]
        for i in range(4):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
                nx, ny = x + dx[i], y + dy[i]
                if not visited[nx][ny] and l <= abs(board[x][y] - board[nx][ny]) <= r:  # 연합 가능
                    united.append([nx, ny])
                    queue.append([nx, ny])
                    visited[nx][ny] = True
    return united


''' 인구 이동 '''
def go(u):
    global board
    p = 0
    for item in u:
        p += board[item[0]][item[1]]
    p = p // len(u)
    for item in u:
        board[item[0]][item[1]] = p


ans = 0
while True:
    visited = [[False] * n for _ in range(n)]
    flag = False  # 인구 이동이 발생했는지 체크
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                group = bfs(deque([(i, j)]))
                if len(group) > 1:  # 인구 이동 발생
                    flag = True
                    go(group)
    if not flag:  # 인구 이동 완료
        print(ans)
        break
    ans += 1
