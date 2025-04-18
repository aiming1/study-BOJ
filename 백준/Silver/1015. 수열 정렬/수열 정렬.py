import copy
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = copy.deepcopy(a)
a.sort()

idx = {k: -1 for k in a}
for i in range(n):
    if idx[a[i]] == -1:
        idx[a[i]] = i

ans = list()
for item in b:
    ans.append(idx[item])
    idx[item] += 1

print(*ans)
