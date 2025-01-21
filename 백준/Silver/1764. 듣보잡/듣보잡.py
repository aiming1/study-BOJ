import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = set()
ans = []

for _ in range(n):
    a.add(input())
for _ in range(m):
    p = input()
    if p in a:
        ans.append(p)


ans.sort()
print(len(ans))
for item in ans:
    print(item[:-1])
