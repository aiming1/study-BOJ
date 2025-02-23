import sys

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * n
adjacent = [[] for _ in range(n)]
arrive = False

for _ in range(m):
    a, b = map(int, input().split())
    adjacent[a].append(b)
    adjacent[b].append(a)


def dfs(start, depth):
    global arrive
    visited[start] = True
    if depth == 5:
        print(1)
        sys.exit()
    for i in adjacent[start]:
        if not visited[i]:
            dfs(i, depth+1)
    visited[start] = False


for i in range(n):
    dfs(i, 1)

print(0)
