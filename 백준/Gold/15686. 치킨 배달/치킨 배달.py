import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
house, chickenHouse = list(), list()
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            house.append([i, j])
        elif line[j] == 2:
            chickenHouse.append([i, j])

chickenDistance = [[0] * len(chickenHouse) for _ in range(len(house))]
for i in range(len(house)):
    for j in range(len(chickenHouse)):
        hx, hy = house[i]
        cx, cy = chickenHouse[j]
        chickenDistance[i][j] = abs(hx - cx) + abs(hy - cy)

survived = list(combinations(range(len(chickenHouse)), m))

ans = set()
for group in survived:
    cnt = 0
    for i in range(len(house)):
        minChickenDistance = float('inf')
        for j in group:
            minChickenDistance = min(minChickenDistance, chickenDistance[i][j])
        cnt += minChickenDistance
    ans.add(cnt)

print(min(ans))
