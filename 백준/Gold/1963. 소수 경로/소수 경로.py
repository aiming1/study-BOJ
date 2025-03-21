import copy
import sys
from collections import deque

input = sys.stdin.readline

prime = [True] * 10002
for i in range(2, 10000):
    for j in range(2, 10000 // i + 1):
        if prime[i * j]:
            prime[i * j] = False


def newnum(num, i):  # i번째 자리를 제거한 수 구하기
    if i == 1:
        return (num // 10) * 10
    elif i == 2:
        return (num // 100) * 100 + (num % 10)
    elif i == 3:
        return (num // 1000) * 1000 + (num % 100)
    elif i == 4:
        return num % 1000


def getnum(num, i):  # i번째 자리 수 구하기
    if i == 1:
        return num % 10
    elif i == 2:
        return (num // 10) % 10
    elif i == 3:
        return (num // 100) % 10
    elif i == 4:
        return num // 1000


def bfs(start, end, visited):
    next_queue = deque([start])
    ans = -1
    while next_queue:
        queue = copy.deepcopy(next_queue)
        next_queue.clear()
        ans += 1
        while queue:
            now = queue.popleft()
            if now == end:
                return ans

            for i in range(1, 5):
                nnow = newnum(now, i)
                exc = getnum(now, i)
                for j in range(10):
                    if j != exc:
                        chk = nnow + j * (10 ** (i - 1))
                        if prime[chk] and not visited[chk] and 1000 <= chk:
                            visited[chk] = True
                            next_queue.append(chk)
    return -1


t = int(input())
for _ in range(t):
    s, e = map(int, input().split())
    a = bfs(s, e, [False] * 10000)
    if a == -1:
        print("Impossible")
    else:
        print(a)
