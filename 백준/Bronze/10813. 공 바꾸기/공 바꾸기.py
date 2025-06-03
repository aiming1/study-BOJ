n, m = map(int, input().split())
balls = [0] + [i for i in range(1, n + 1)]
def swap(i, j):
    global balls
    tmp = balls[i]
    balls[i] = balls[j]
    balls[j] = tmp

for _ in range(m):
    i, j = map(int, input().split())
    swap(i, j)

print(*balls[1:])
