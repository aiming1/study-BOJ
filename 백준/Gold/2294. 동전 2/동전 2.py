import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = set()
for _ in range(n):
    coin.add(int(input()))
coin = list(coin)
coin.sort()

dp = [1e9] * (k + 1)
dp[0] = 0

for c in coin:
    for i in range(c, k + 1):
        dp[i] = min(dp[i], dp[i - c] + 1)

print(dp[-1] if dp[-1] != 1e9 else -1)
