import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [True] + [False] * n


def dfs(now):
    for i in range(1, n + 1):
        if not visited[i] and graph[now][i]:
            visited[i] = True
            dfs(i)


ans = 0
for i in range(1, n + 1):
    if visited[i]:
        continue
    dfs(i)
    ans += 1

print(ans)
