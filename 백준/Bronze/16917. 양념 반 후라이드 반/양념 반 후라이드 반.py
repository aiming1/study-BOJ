import sys

input = sys.stdin.readline

a, b, c, x, y = map(int, input().split())

if 2 * c < a + b:
    print(min(min(x, y) * 2 * c + abs(x - y) * (a if x > y else b), max(x, y) * c * 2))
else:
    print(x * a + y * b)
