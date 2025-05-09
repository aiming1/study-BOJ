import sys

input = sys.stdin.readline

a, b = ' ' + str(input())[:-1], ' ' + str(input())[:-1]
dp = [[[0, '\n'] for _ in range(len(b))] for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j][0] = dp[i - 1][j - 1][0] + 1
            dp[i][j][1] = dp[i - 1][j - 1][1] + a[i]
        else:
            dp[i][j][0] = max(dp[i - 1][j][0], dp[i][j - 1][0])
            dp[i][j][1] = dp[i - 1][j][1] if dp[i - 1][j][0] > dp[i][j - 1][0] else dp[i][j - 1][1]

print(*dp[-1][-1])
