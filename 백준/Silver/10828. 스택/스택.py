import sys

input = sys.stdin.readline

n = int(input())
s = list()

for _ in range(n):
    m = list(map(str, input().split()))
    if m[0] == 'push':
        s.append(m[1])
    elif m[0] == 'pop':
        print(s.pop() if len(s) else -1)
    elif m[0] == 'size':
        print(len(s))
    elif m[0] == 'empty':
        print(0 if len(s) else 1)
    else:
        print(s[-1] if len(s) else -1)
