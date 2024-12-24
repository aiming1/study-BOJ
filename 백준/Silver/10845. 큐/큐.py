import sys

input = sys.stdin.readline

n = int(input())
q = list()

for _ in range(n):
    r = list(map(str, input().split()))

    if r[0] == 'push':
        q.append(r[1])
    elif r[0] == 'pop':
        if not len(q):
            print(-1)
        else:
            print(q[0])
            q = q[1:]
    elif r[0] == 'size':
        print(len(q))
    elif r[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif r[0] == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif r[0] == 'back':
        if len(q):
            print(q[-1])
        else:
            print(-1)
