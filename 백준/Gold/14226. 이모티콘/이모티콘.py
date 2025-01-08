import sys
from collections import deque

input = sys.stdin.readline

s = int(input())
dist = [[0] * 1001 for i in range(1001)]

'''
dist[screen][clip] = 화면에 띄워진 이모티콘이 screen개, 클립보드의 이모티콘이 clip개일 때의 시간 최솟값
1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장하는 경우
- dist[screen][screen] = dist[screen][clip] + 1
2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣는 경우
- dist[screen + clip][clip] = dist[screen][clip] + 1
3. 화면에 있는 이모티콘 중 하나를 삭제하는 경우
- dist[screen - 1][clip] = dist[screen][clip] + 1 
'''

queue = deque([(1, 0)])
ans = 1e9


def bfs():
    global ans

    while queue:
        now_screen, now_clip = queue.popleft()
        if now_screen == s:
            for item in dist[s]:
                if 0 < item < ans:
                    ans = item
            break

        for change in (now_screen, now_screen + now_clip, now_screen - 1):
            if 0 <= change < 1001:
                if change == now_screen and dist[now_screen][change] == 0:
                    dist[now_screen][change] = dist[now_screen][now_clip] + 1
                    queue.append([now_screen, change])
                elif dist[change][now_clip] == 0:
                    dist[change][now_clip] = dist[now_screen][now_clip] + 1
                    queue.append([change, now_clip])


bfs()
print(ans)
