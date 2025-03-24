import sys
from collections import deque

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
visited = [True] + [False] * f
visited[s] = True


def bfs():
    queue = deque([(s, 0)])
    while queue:
        now, now_b = queue.popleft()
        if now == g:
            return now_b
        for go in (u, -d):
            next = now + go
            if 1 <= next <= f:
                if not visited[next]:
                    visited[next] = True
                    queue.append([next, now_b + 1])
    return "use the stairs"


print(bfs())
