import sys
from collections import deque
input = sys.stdin.readline

testCase = int(input())
for _ in range(testCase):
    h, w = map(int, input().split())

    # 상근이의 위치를 특정화 하기 어렵기 때문에 graph의 상화좌우에 빈칸을 더해준다.
    graph = [["." for _ in range(w+2)]]
    for y in range(h):
        row = list(input()[:-1])
        graph.append(["."] + row + ["."])
    graph.append(["." for _ in range(w+2)])

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    # y, x에서 출발했을 때 각 지점까지 문을 얼마나 열고 가야하는 지 값 출력
    def bfs(y, x):
        dq = deque([(y, x)])
        dist = [[-1 for _ in range(w+2)] for _ in range(h+2)]
        dist[y][x] = 0
        while dq:
            y, x = dq.pop()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < w+2 and 0 <= ny < h+2 and graph[ny][nx] != "*" and dist[ny][nx] == -1:
                    if graph[ny][nx] == "#":
                        dist[ny][nx] = dist[y][x] + 1
                        dq.appendleft((ny, nx))
                    else:
                        dist[ny][nx] = dist[y][x]
                        dq.append((ny, nx)) 

        return dist

    # 수감자 위치 찾기
    prisoner = []
    for y, row in enumerate(graph):
        for x, v in enumerate(row):
            if v == "$":
                prisoner.append((y, x))

    # 수감자들의 위치와 상근이 위치에서 각각 bfs를 돌려준다.   
    dist1 = bfs(prisoner[0][0], prisoner[0][1])
    dist2 = bfs(prisoner[1][0], prisoner[1][1])
    dist3 = bfs(0,0)

    # 합이 최소가 되는 값을 찾는다. 단, 위치가 문이라면 -2를 해준다.
    result = float("inf")
    for y in range(h+2):
        for x in range(w+2):
            s = dist1[y][x] + dist2[y][x] + dist3[y][x]
            if graph[y][x] == "#":
                s -= 2

            if s >= 0:
                result = min(result, s)

    print(result)