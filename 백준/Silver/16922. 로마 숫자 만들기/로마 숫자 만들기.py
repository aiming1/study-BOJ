import copy
import sys

input = sys.stdin.readline

visited = [False] * 1001
visited[1] = visited[5] = visited[10] = visited[50] = True

for _ in range(int(input()) - 1):
    this_visited = [False] * 1001
    for i in range(1, 1001):
        if visited[i]:
            for t in (1, 5, 10, 50):
                this_visited[i + t] = True
    visited = copy.deepcopy(this_visited)

ans = 0
for i in range(1, 1001):
    if visited[i]:
        ans += 1

print(ans)
