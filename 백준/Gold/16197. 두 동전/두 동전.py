import copy
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(str(input())[:-1])

coin = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            coin.append([i, j])

dx = [-1, 0, 1, 0]  # 위, 왼, 아래, 오
dy = [0, -1, 0, 1]
next = deque(coin)

'''
 안 되는 경우
 1. 이전의 위치로 되돌아감
 2. 두 동전의 이동 방향이 모두 벽
 3. 이동 시 두 동전이 겹쳐짐
 4. 이동 시 두 동전이 함께 떨어짐
 '''


def bfs():
    global ans, visited, next, next2
    while next:
        ans += 1
        next2 = copy.deepcopy(next)
        next.clear()

        while next2:
            c = [next2.popleft(), next2.popleft()]
            if ans > 10:
                return

            for i in range(4):
                x = [c[0][0] + dx[i], c[1][0] + dx[i]]  # 앞으로의 이동 방향 저장
                y = [c[0][1] + dy[i], c[1][1] + dy[i]]

                ''' 이동했을 때 동전이 떨어지는 경우 '''
                if not (0 <= x[0] < n and 0 <= y[0] < m) and not (0 <= x[1] < n and 0 <= y[1] < m):  # 둘 다 떨어짐(4번 경우)
                    continue  # 이동하지 않음
                elif not (0 <= x[0] < n and 0 <= y[0] < m) or not (0 <= x[1] < n and 0 <= y[1] < m):  # 둘 중 하나만 떨어짐
                    return

                ''' 이동했을 때 동전이 떨어지지 않는 경우 '''
                for j in range(2):  # 실제 이동 좌표로 수정
                    if board[x[j]][y[j]] == '#':  # 이동 좌표에 벽이 있으면 이동하지 않음
                        x[j] = c[j][0]
                        y[j] = c[j][1]

                if x[0] == x[1] and y[0] == y[1]:  # 두 동전의 좌표가 같은 경우(3번 경우)
                    continue  # 이동하지 않음
                if x[0] == c[0][0] and x[1] == c[1][0] and y[0] == c[0][1] and y[1] == c[1][1]:  # 두 동전 모두 이동 불가(2번 경우)
                    continue  # 이동하지 않음

                next.append([x[0], y[0]])
                next.append([x[1], y[1]])
        if not next:
            ans = 11
            return


ans = 0
bfs()
if ans > 10:
    print(-1)
else:
    print(ans)
