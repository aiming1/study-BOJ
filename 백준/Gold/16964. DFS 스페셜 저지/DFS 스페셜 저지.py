import sys

input = sys.stdin.readline

n = int(input())
arr = [set() for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    arr[a].add(b)
    arr[b].add(a)
order = list(map(int, input().split()))


def check():
    if order[0] != 1:
        return 0
    stack = [order[0]]
    for i in range(1, n):
        value = order[i]
        while stack and value not in arr[stack[-1]]:
            stack.pop()
            if not stack:
                return 0
        stack.append(value)
    return 1


print(check())
