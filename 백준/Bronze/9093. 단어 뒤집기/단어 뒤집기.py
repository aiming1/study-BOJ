import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = list(map(str, input().split()))
    rs = list()
    for word in s:
        rword = ''
        for l in word:
            rword = l + rword
        rs.append(rword)
    print(*rs)
