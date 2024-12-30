import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
queue = deque()


def chess(d, c, q):
    while len(q):
        now = q.popleft()
        for i in range(8):
            goto = [now[0] + dx[i], now[1] + dy[i]]  # 향할 방향

            if l > goto[0] >= 0 and l > goto[1] >= 0:  # 이동 위치가 허용 범위 내에 있고
                if c[goto[0]][goto[1]] == 0:  # 이동 위치를 한 번도 방문하지 않았으면
                    c[goto[0]][goto[1]] = c[now[0]][now[1]] + 1  # 그 위치로 향하기 위한 최단 거리를 +1
                    q.append(goto)  # 그 위치를 큐에 추가

            if goto == d:  # 목적지에 도달했다면 반복 끝
                break

    print(c[d[0]][d[1]])


for _ in range(t):
    l = int(input())
    start = list(map(int, input().split()))
    dest = list(map(int, input().split()))
    cnt = [[0] * l for _ in range(l)]

    if start == dest:
        print(0)
        continue

    queue.clear()
    queue.append(start)
    chess(dest, cnt, queue)
