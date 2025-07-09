import sys
from itertools import permutations

input = sys.stdin.readline

a, b = map(int, input().split())
a = list(str(a))
a.sort(reverse=True)
for case in permutations(a, len(a)):
    s = ''
    for item in case:
        s += item

    if len(s) != len(str(int(s))):
        continue

    if int(s) < b:
        print(int(s))
        exit()

print(-1)
