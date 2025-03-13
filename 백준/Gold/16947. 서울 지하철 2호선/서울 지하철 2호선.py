import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(x, tmp):
    global cycle
    visited[x] = True
    tmp.append(x)
    
    for next in graph[x]:
        if visited[next]:
            if next in tmp:
                if len(tmp[tmp.index(next):]) >= 3:
                    cycle = set(tmp[tmp.index(next):])
                    return True
            continue
        dfs(next, tmp)
        tmp.pop()


n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    if not visited[i]:
        tmp = []
        if dfs(i, tmp):
            print(cycle)  
            break

d = [-1] * (n + 1)

def setDepth(x, depth):
    if x in cycle:
        d[x] = 0
        depth = 0
    else:
        d[x] = depth
    
    for next in graph[x]:
        if d[next] >= 0:
            continue
        setDepth(next, depth + 1)

setDepth(list(cycle)[0], 0)

for i in range(1, n + 1):
    print(d[i], end=" ")