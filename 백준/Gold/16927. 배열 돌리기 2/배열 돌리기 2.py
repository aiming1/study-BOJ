import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())
input_array = [[0] * (m + 1)]
for _ in range(n):
    input_array.append([0] + list(map(int, input().split())))
ans_array = [[0] * (m + 1) for _ in range(n + 1)]


for rotate in range(1, min(n, m) // 2 + 1):
    ''' 줄줄이 만들기 '''
    queue = deque()
    for i in range(rotate, m - rotate + 2):  # 상
        queue.append(input_array[rotate][i])
    for i in range(rotate + 1, n - rotate + 2):  # 우
        queue.append(input_array[i][m - rotate + 1])
    for i in range(m - rotate, rotate - 1, -1):  # 하
        queue.append(input_array[n - rotate + 1][i])
    for i in range(n - rotate, rotate, -1):  # 좌
        queue.append(input_array[i][rotate])

    ''' 회전 '''
    for i in range(r % len(queue)):
        queue.rotate(-1)

    ''' 붙여넣기 '''
    for i in range(rotate, m - rotate + 2):  # 상
        ans_array[rotate][i] = queue.popleft()
    for i in range(rotate + 1, n - rotate + 2):  # 우
        ans_array[i][m - rotate + 1] = queue.popleft()
    for i in range(m - rotate, rotate - 1, -1):  # 하
        ans_array[n - rotate + 1][i] = queue.popleft()
    for i in range(n - rotate, rotate, -1):  # 좌
        ans_array[i][rotate] = queue.popleft()

''' 출력 '''
for item in ans_array[1:]:
    print(*item[1:])
