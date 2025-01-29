import sys

input = sys.stdin.readline

n, m = map(int, input().split())
price = 1e9
store = [[] for _ in range(2)]
for _ in range(m):
    a, b = map(int, input().split())
    store[0].append(a)
    store[1].append(b)

one = min(store[0])
two = min(store[1])
price = min(price, one * (n // 6 + 1), one * (n // 6) + two * (n % 6), two * n)

print(price)

