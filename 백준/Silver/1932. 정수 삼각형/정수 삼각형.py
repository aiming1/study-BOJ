import sys

input = sys.stdin.readline

n = int(input())
t = [0]

for _ in range(n):
    l = list(map(int, input().split()))
    for i in l:
        t.append(i)

dp = [0, t[1]] + [0] * (len(t) - 2)

level = 2
count = 1
for i in range(2, len(t)):
    if count == 1:
        dp[i] = t[i] + dp[i - level + 1]
    elif count == level:
        dp[i] = t[i] + dp[i - level]
        level += 1
        count = 1
        continue
    else:
        dp[i] = t[i] + max(dp[i - level], dp[i - level + 1])
    count += 1

print(max(dp))
