import sys

input = sys.stdin.readline

n, m = map(int, input().split())
friend = {i:set() for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    friend[a].add(b)
    friend[b].add(a)
ans = float('inf')

for a in range(1, n - 1):
    for b in friend[a]:
        if b < a:
            continue
        for c in friend[b]:
            if c < b:
                continue
            if c in friend[a]:
                ans = min(ans,
                          len(friend[a]) + len(friend[b]) + len(friend[c]) - 6)

print(ans if ans != float('inf') else -1)
