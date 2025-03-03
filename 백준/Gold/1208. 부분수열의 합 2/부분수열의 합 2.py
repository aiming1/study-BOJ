import sys
from itertools import combinations
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n, s = map(int, input().split())
input_list = list(map(int, input().split()))
left, right = input_list[:n // 2], input_list[n // 2:]


def get_sum(arr):
    sumarr = list()
    for i in range(1, len(arr) + 1):
        for a in combinations(arr, i):
            sumarr.append(sum(a))
    sumarr.sort()
    return sumarr


def getNum(arr, find):
    return bisect_right(arr, find) - bisect_left(arr, find)


left_sum = get_sum(left)
right_sum = get_sum(right)
ans = 0

for l in left_sum:
    find = s - l
    ans += getNum(right_sum, find)

ans += getNum(left_sum, s)
ans += getNum(right_sum, s)

print(ans)
