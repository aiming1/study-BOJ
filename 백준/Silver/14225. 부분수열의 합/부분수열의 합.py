import sys

input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
a = set()


def dfs(idx, now):
    if idx == n:
        return

    ''' 어떠한 원소는 부분 수열에 포함되거나 / 포함되지 않거나 둘 중 하나 '''
    ''' idx = 현재 탐색 중인 숫자 -> 이 숫자를 수열에 포함하거나 / 포함하지 않아 가며 모든 케이스를 탐색 '''
    a.add(now + s[idx])
    dfs(idx + 1, now + s[idx])  # 현재 숫자를 부분 수열에 포함
    dfs(idx + 1, now)  # 현재 숫자를 부분 수열에 포함하지 않음


dfs(0, 0)

a = sorted(a)
ans = 1
for num in a:
    if num == ans:
        ans += 1
    elif num > ans:
        break

print(ans)
