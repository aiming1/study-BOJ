import sys
from collections import deque

input = sys.stdin.readline

''' 입력 '''
m, n = map(int, input().split())
maze = ['2' * (m + 1)]

for i in range(n):
    maze.append('2' + str(input())[:-1])

''' 로직 '''
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque([(1, 1)])  # 출발 지점
ans = [[-1] * (m + 1) for _ in range(n + 1)]  # 벽 개수 저장하는 리스트
ans[1][1] = 0  # 출발 지점의 벽 뿌숨 개수는 0


def bfs():
    while queue:
        now_x, now_y = queue.popleft()

        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]
            if 0 <= next_x <= n and 0 <= next_y <= m:  # 다음으로 향할 좌표가 배열 범위 안이고
                if ans[next_x][next_y] == -1:  # 해당 좌표를 중심으로 탐색한 적이 없으면
                    if maze[next_x][next_y] == '0':  # 그 좌표의 미로 값이 0일 때
                        ans[next_x][next_y] = ans[now_x][now_y]  # 뚫는 벽 개수는 추가 안 됨
                        queue.appendleft([next_x, next_y])
                    else:  # 그 좌표의 미로 값이 1일 때
                        ans[next_x][next_y] = ans[now_x][now_y] + 1  # 벽 뚫기 지수 +1
                        queue.append([next_x, next_y])


bfs()
print(ans[n][m])
