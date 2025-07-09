import sys
from itertools import combinations

input = sys.stdin.readline

n, l, r, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

for i in range(2, n + 1):
    for c in combinations(a, i):
        if max(c) - min(c) >= x and l <= sum(c) <= r:
            ans += 1

print(ans)
