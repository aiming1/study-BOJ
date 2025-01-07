import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque()
visited = [-1] * 100001


def bfs():
    while queue:
        now = queue.popleft()
        if now == k:
            print(visited[k])
            break

        for next in (now * 2, now + 1, now - 1):
            if 0 <= next < 100001 and visited[next] == -1:
                visited[next] = visited[now] + 1
                queue.append(next)


queue.append(n)
visited[n] = 0

bfs()
