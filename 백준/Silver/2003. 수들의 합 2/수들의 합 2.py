import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

for i in range(n):
    num = a[i]
    if num == m:
        ans += 1
        continue

    for j in range(i + 1, n):
        num += a[j]
        if num == m:
            ans += 1
            break
        if num > m:
            break

print(ans)
