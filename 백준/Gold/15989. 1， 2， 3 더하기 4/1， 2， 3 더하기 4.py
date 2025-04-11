import sys

input = sys.stdin.readline

dp = [1, 1, 2, 3, 4]
''' dp[n] = 1 + dp[n - 2] + dp[n - 3] - dp[n - 5]'''

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(len(dp), n + 1):
        dp.append(1 + dp[i - 2] + dp[i - 3] - dp[i - 5])
    print(dp[n])
