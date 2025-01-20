import sys

input = sys.stdin.readline

t = int(input())
cog = ['']
for _ in range(t):
    cog.append(str(input())[:-1])


def rotate(wheel, dir):
    global cog

    rotate_cog = [0] * (t + 1)  # 톱니바퀴별 회전 방향을 기록하는 리스트
    rotate_cog[wheel] = dir
    for i in range(wheel + 1, t + 1):  # 대상 톱니바퀴와 오른쪽 톱니바퀴가 맞닿음
        if cog[i][6] == cog[i - 1][2]:
            break
        rotate_cog[i] = rotate_cog[i - 1] * (-1)

    for i in range(wheel - 1, 0, -1):  # 대상 톱니바퀴와 왼쪽 톱니바퀴가 맞닿음
        if cog[i][2] == cog[i + 1][6]:
            break
        rotate_cog[i] = rotate_cog[i + 1] * (-1)

    for i in range(1, t + 1):
        if rotate_cog[i] == 0:  # 회전하지 않음
            continue
        elif rotate_cog[i] == 1:  # 시계 방향 회전
            cog[i] = cog[i][-1] + cog[i][:-1]
        else:  # 반시계 방향 회전
            cog[i] = cog[i][1:] + cog[i][0]


k = int(input())
for _ in range(k):
    n, d = map(int, input().split())
    rotate(n, d)

ans = 0
for a in range(1, t + 1):
    if cog[a][0] == '1':
        ans += 1
print(ans)
