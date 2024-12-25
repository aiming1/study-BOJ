import sys

input = sys.stdin.readline

n = int(input())
d = list()

for _ in range(n):
    i = list(map(str, input().split()))

    if i[0] == 'push_front':
        d.insert(0, i[1])
    elif i[0] == 'push_back':
        d.append(i[1])
    elif i[0] == 'pop_front':
        if len(d):
            print(d[0])
            d = d[1:]
        else:
            print(-1)
    elif i[0] == 'pop_back':
        if len(d):
            print(d[-1])
            d.pop()
        else:
            print(-1)
    elif i[0] == 'size':
        print(len(d))
    elif i[0] == 'empty':
        if len(d):
            print(0)
        else:
            print(1)
    elif i[0] == 'front':
        if len(d):
            print(d[0])
        else:
            print(-1)
    elif i[0] == 'back':
        if len(d):
            print(d[-1])
        else:
            print(-1)

