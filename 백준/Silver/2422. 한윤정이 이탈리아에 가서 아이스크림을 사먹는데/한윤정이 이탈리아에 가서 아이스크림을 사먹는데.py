import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cant_eat = set()
for _ in range(m):
    a, b = map(int, input().split())
    cant_eat.add((a, b))
    cant_eat.add((b, a))
ans = 0

def dfs(cnt, selected):
    global ans
    if cnt == 3:
        ans += 1
        return

    for i in range(selected[-1] + 1, n + 1):
        for item in selected:
            if (i, item) in cant_eat:
                break
        else:
            dfs(cnt + 1, selected + [i])

for i in range(1, n - 1):
    dfs(1, [i])
print(ans)
