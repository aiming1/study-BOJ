import copy
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = list()
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[-1][j] == 9:
            next_queue = deque([(i, j)])
            sx, sy = i, j

shark = 2
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def fish_chk():  # 먹을 수 있는 물고기가 있는지 여부 체크
    for line in board:
        for item in line:
            if item < shark:
                return True
    return False


''' bfs - 가장 가까운 먹을 수 있는 물고기를 탐색 '''
def bfs(visited):
    dis = 0  # 물고기까지의 거리
    fishes = list()
    while next_queue:
        queue = copy.deepcopy(next_queue)
        next_queue.clear()
        dis += 1
        while queue:
            now = queue.popleft()
            x, y = now[0], now[1]
            for i in range(4):
                if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
                    nx, ny = x + dx[i], y + dy[i]
                    if not visited[nx][ny] and board[nx][ny] <= shark:  # 이동 가능
                        next_queue.append([nx, ny])
                        visited[nx][ny] = True
                        if 0 < board[nx][ny] < shark:  # 물고기 먹음
                            fishes.append([nx, ny])
        if fishes:  # 먹을 수 있는 물고기 발견
            fishes.sort()
            next_queue.clear()
            return [fishes[0][0], fishes[0][1], dis]  # 먹을 물고기 위치, 거기까지의 거리
    return [-1, -1, dis]  # 먹을 수 있는 물고기가 있지만 도달할 수 없음


ans = 0
eat = 0
while fish_chk():
    visited = [[False] * n for _ in range(n)]
    visited[sx][sy] = True
    board[sx][sy] = 0
    next = bfs(visited)
    if next[0] == -1:
        print(ans)
        exit()
    sx, sy = next[0], next[1]
    ans += next[2]
    next_queue.append([sx, sy])
    board[sx][sy] = 9
    eat += 1
    if shark == eat:
        shark += 1
        eat = 0

print(ans)
