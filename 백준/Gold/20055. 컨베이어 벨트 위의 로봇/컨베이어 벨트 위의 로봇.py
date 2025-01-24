import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
robot = [False] * n

zero = 0
ans = 0
while True:
    ans += 1

    ''' 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다 '''
    a = [a[-1]] + a[:-1]
    robot = [robot[-1]] + robot[:-1]
    robot[n - 1] = False

    ''' 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. '''
    for i in range(n - 2, -1, -1):
        if robot[i] and not robot[i + 1]:
            if a[i + 1] > 0:
                a[i + 1] -= 1
                robot[i] = False
                robot[i + 1] = True
                if a[i + 1] == 0:
                    zero += 1
    robot[n - 1] = False

    ''' 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다. '''
    if a[0] > 0:
        robot[0] = True
        a[0] -= 1

    ''' 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다. '''
    if a.count(0) >= k:
        break

print(ans)
