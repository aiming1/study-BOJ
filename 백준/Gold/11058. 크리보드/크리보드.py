import sys

input = sys.stdin.readline

n = int(input())
dp = [i for i in range(n + 1)]

for i in range(4, n + 1):
    for j in range(i, n + 1):
        dp[j] = max(dp[j], dp[i - 3] * (j - i + 2))

print(dp[n])
