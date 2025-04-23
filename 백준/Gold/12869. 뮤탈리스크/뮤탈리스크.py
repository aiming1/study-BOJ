import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

n, scv = int(input()), list(map(int, input().split()))
while len(scv) < 3:
    scv.append(0)
attack = [t for t in permutations([9, 3, 1], 3)]
dp = [[[0] * (scv[2] + 1) for _ in range(scv[1] + 1)] for _ in range(scv[0] + 1)]

queue = deque([(scv[0], scv[1], scv[2], 0)])
while queue:
    na, nb, nc, hit = queue.popleft()
    for a, b, c in attack:
        aa = na - a if na - a > 0 else 0
        bb = nb - b if nb - b > 0 else 0
        cc = nc - c if nc - c > 0 else 0
        if dp[aa][bb][cc] == 0:
            dp[aa][bb][cc] = hit + 1
            queue.append([aa, bb, cc, hit + 1])

print(dp[0][0][0])
