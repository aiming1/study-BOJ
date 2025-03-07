import bisect
import sys

input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))


def getsum(l, lt):
    l_sum = list()
    for i in range(lt):
        num = 0
        for j in range(i, lt):
            num += l[j]
            l_sum.append(num)
    return l_sum


def find(arr1, arr2, num):
    return (bisect.bisect_right(arr1, num) - bisect.bisect_left(arr1, num))\
           * (bisect.bisect_right(arr2, t - num) - bisect.bisect_left(arr2, t - num))


a_sum = getsum(a, n)
b_sum = getsum(b, m)
a_sum.sort()
b_sum.sort()
b_chk = set(b_sum)
i, ans = 0, 0


while i < len(a_sum):
    if t - a_sum[i] in b_chk:
        ans += find(a_sum, b_sum, a_sum[i])
    i = bisect.bisect_right(a_sum, a_sum[i])

print(ans)
