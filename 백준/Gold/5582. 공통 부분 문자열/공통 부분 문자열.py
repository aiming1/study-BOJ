import sys

input = sys.stdin.readline

a, b = ' ' + str(input())[:-1], ' ' + str(input())[:-1]
dp = [[0] * len(b) for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1

m = 0
for line in dp:
    m = max(m, max(line))

print(m)
