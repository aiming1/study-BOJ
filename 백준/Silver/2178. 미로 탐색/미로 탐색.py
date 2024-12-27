import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maze = ['0' * (m + 2)]
for _ in range(n):
    maze.append('0' + str(input())[:-1] + '0')
maze += ['0' * (m + 2)]

visited = [[False] * (m + 2) for _ in range(n + 2)]
ans = [[10000] * (m + 2) for _ in range(n + 2)]
ans[1][1] = 1

''' bfs로 다시 풀자 '''
def bfs():
    queue = deque()
    queue.append([1, 1])
    visited[1][1] = True
    while queue:
        now = queue.popleft()
        cnt = min(ans[now[0] - 1][now[1]], ans[now[0] + 1][now[1]], ans[now[0]][now[1] + 1], ans[now[0]][now[1] - 1], ans[now[0]][now[1]]) + 1
        ans[now[0]][now[1]] = min(ans[now[0]][now[1]], cnt)
        if not visited[now[0] + 1][now[1]] and maze[now[0] + 1][now[1]] == '1':  # 아래로 갈 수 있는 경우
            queue.append([now[0] + 1, now[1]])
            visited[now[0] + 1][now[1]] = True
        if not visited[now[0] - 1][now[1]] and maze[now[0] - 1][now[1]] == '1':  # 위로 갈 수 있는 경우
            queue.append([now[0] - 1, now[1]])
            visited[now[0] - 1][now[1]] = True
        if not visited[now[0]][now[1] + 1] and maze[now[0]][now[1] + 1] == '1':  # 오른쪽으로 갈 수 있는 경우
            queue.append([now[0], now[1] + 1])
            visited[now[0]][now[1] + 1] = True
        if not visited[now[0]][now[1] - 1] and maze[now[0]][now[1] - 1] == '1':  # 왼쪽으로 갈 수 있는 경우
            queue.append([now[0], now[1] - 1])
            visited[now[0]][now[1] - 1] = True

bfs()
print(ans[n][m])
