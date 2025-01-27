import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    num = 1
    for _ in range(b):
        num = (num * a) % 10
    if num != 0:
        print(num)
    else:
        print(10)
