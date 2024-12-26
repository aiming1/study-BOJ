import sys
input = sys.stdin.readline

n = int(input())
house = list()
house.append('0' * (n + 1))
for _ in range(n):
    house.append('0' + str(input())[:-1])

visited = [[False] * (n + 1) for _ in range(n + 1)]


t = list()
def dfs(a, b):
    for i in range(a, n + 1):
        for j in range(b, n + 1):
            if house[i][j] == '0':
                return

            if not visited[i][j]:
                visited[i][j] = True
                t.append([i, j])
                if j != n:
                    if house[i][j + 1] == '1' and not visited[i][j + 1]:
                        dfs(i, j + 1)
                if i != n:
                    if house[i + 1][j] == '1' and not visited[i + 1][j]:
                        dfs(i + 1, j)
                if house[i][j - 1] == '1' and not visited[i][j - 1]:
                    dfs(i, j - 1)
                if house[i - 1][j] == '1' and not visited[i - 1][j]:
                    dfs(i - 1, j)


ans = 0
ans2 = list()
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if house[i][j] == '1' and not visited[i][j]:
            dfs(i, j)
            ans += 1
            ans2.append(len(t))
            t.clear()

ans2.sort()
print(ans, *ans2, sep="\n")