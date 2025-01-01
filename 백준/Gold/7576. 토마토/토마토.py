import copy
import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
tomatoes = list()
start = deque()
row_tomato = 0  # 생 토마토의 개수
good_tomato = 0  # 익힌 토마토의 개수

for _ in range(n):
    tomatoes.append(list(map(int, input().split())))
    for item in tomatoes[-1]:  # 생 토마토 개수 세기
        if item == 0:
            row_tomato += 1

if row_tomato == 0:  # 생 토마토가 없는 상태 == 모든 토마토가 익은 상태 -> 0 출력
    print(0)
    sys.exit()

for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            start.append([i, j])

dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]

now_queue = start  # 지금 탐색할 토마토 무리
next_queue = deque()  # 다음에 탐색할 토마토 무리
days = 0  # 토마토 익는 날짜


def bfs():
    global start, good_tomato, tomatoes, now_queue, next_queue, days, dx, dy

    while len(now_queue) or len(next_queue):
        while len(now_queue):  # 탐색 가능 토마토가 남아 있으면 반복
            now = now_queue.popleft()  # 지금 탐색 중인 토마토
            for a in range(4):
                x = now[0] + dx[a]
                y = now[1] + dy[a]
                if 0 <= x < n and 0 <= y < m:  # 지금 탐색 중인 토마토 상하좌우가 이동 가능하면
                    if tomatoes[x][y] == 0:  # 이동 위치의 토마토가 생 토마토인지 확인하고
                        next_queue.append([x, y])  # 생 토마토일 시 다음 탐색 대상에 추가
                        tomatoes[x][y] = 1  # 추가한 생 토마토는 구운 토마토로 바꿔 줌
                        good_tomato += 1  # 구운 토마토의 총 개수 추가
        now_queue = copy.deepcopy(next_queue)
        next_queue.clear()
        days += 1


bfs()

if row_tomato != good_tomato:  # 처음부터 생 토마토가 모두 익지 못하는 상황이었다면
    print(-1)
else:
    print(days - 1)