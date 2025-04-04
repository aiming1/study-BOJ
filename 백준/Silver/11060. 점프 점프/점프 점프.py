import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [0] + [-1] * (n - 1)

queue = deque([0])
while queue:
    now = queue.popleft()
    for i in range(1, a[now] + 1):
        if now + i < n:
            next = now + i
            if dp[next] == -1:
                queue.append(next)
                dp[next] = dp[now] + 1

print(dp[-1])
