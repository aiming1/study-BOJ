import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    if a % 10 == 0:
        print(10)
    else:
        print((a ** ((b % 4) + 4)) % 10)