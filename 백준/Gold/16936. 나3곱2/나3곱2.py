import copy
import sys

input = sys.stdin.readline

n, ori_b = int(input()), set(map(int, input().split()))

def dfs(x, a, b):
    if len(a) == n:
        print(*a)
        exit()

    if x % 2 == 0 and x // 2 in b:
        dfs(x // 2, [x // 2] + a, b - {x // 2})
    elif x * 3 in b:
        dfs(x * 3, [x * 3] + a, b - {x * 3})

for item in ori_b:
    dfs(item, [item], copy.deepcopy(ori_b))
