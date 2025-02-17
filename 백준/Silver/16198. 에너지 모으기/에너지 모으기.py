import sys

input = sys.stdin.readline


n = int(input())
w = list(map(int, input().split()))
ans = set()


def dfs(idx, now_list, s):
    global n

    if idx == n - 2:
        ans.add(s)
        return

    for i in range(1, len(now_list) - 1):
        dfs(idx + 1, now_list[:i] + now_list[i + 1:], s + now_list[i - 1] * now_list[i + 1])


dfs(0, w, 0)
print(max(ans))
