import copy
import sys

input = sys.stdin.readline

n, s, m = map(int, input().split())
v = list(map(int, input().split()))
s1 = {s}

''' 점화식: s +- v[1] +- v[2] +- ... +- v[n] '''

for now in v:
    s2 = set()
    for p in s1:
        if p + now <= m:
            s2.add(p + now)
        if p - now >= 0:
            s2.add(p - now)
    s1 = copy.deepcopy(s2)
    if not s1:
        print(-1)
        exit()

print(max(s1))
