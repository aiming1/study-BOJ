import sys

input = sys.stdin.readline

''' 가능한 연산자 조합을 dfs로 구하고 계산 '''
n = int(input())
a = list(map(int, input().split()))
cal = list(map(int, input().split()))  # + - * /
max_ans = int(-1e9)
min_ans = int(1e9)


def dfs(idx, c, num):
    global max_ans, min_ans

    if idx == n - 1:
        max_ans = max(max_ans, num)
        min_ans = min(min_ans, num)
        return

    for i in range(4):
        if c[i] > 0:
            if i == 0:  # +
                tmp = num + a[idx + 1]
            elif i == 1:  # -
                tmp = num - a[idx + 1]
            elif i == 2:  # *
                tmp = num * a[idx + 1]
            else:  # /
                tmp = abs(num) // a[idx + 1]
                if num < 0:
                    tmp *= -1
            dfs(idx + 1, c[:i] + [c[i] - 1] + c[i + 1:], tmp)


dfs(0, cal, a[0])
print(max_ans)
print(min_ans)
