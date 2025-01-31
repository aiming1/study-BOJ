import sys

input = sys.stdin.readline

n = int(input())
ans = str(input())[:-1]

for _ in range(n - 1):
    cop = str(input())[:-1]
    for i in range(len(cop)):
        if ans[i] != cop[i] and ans[i] != '?':
            ans = ans[:i] + '?' + ans[i + 1:]

print(ans)
