import sys

input = sys.stdin.readline

n, r = map(int, input().split())
a = []
for _ in range(2 ** n):
    a.append(list(map(int, input().split())))
a_size = 2 ** n

for _ in range(r):
    k, l = map(int, input().split())
    level = 2 ** l

    if k == 1:
        ''' 1: 각 부분 배열을 상하 반전 '''
        for i in range(0, a_size, level):
            for j in range(0, a_size, level):
                for r in range(level // 2):
                    a[i + r][j:j + level], a[i + level - r - 1][j:j + level]\
                        = a[i + level - r - 1][j:j + level], a[i + r][j:j + level]
    elif k == 2:
        ''' 2: 각 부분 배열을 좌우 반전 '''
        for i in range(0, a_size, level):
            for j in range(0, a_size, level):
                for r in range(level):
                    for c in range(level // 2):
                        a[i + r][j + c], a[i + r][j + level - c - 1]\
                            = a[i + r][j + level - c - 1], a[i + r][j + c]
    elif k == 3:
        ''' 3. 각 부분 배열을 오른쪽으로 90도 회전 '''
        for i in range(0, a_size, level):
            for j in range(0, a_size, level):
                tmp = [[0] * level for _ in range(level)]
                for r in range(level):
                    for c in range(level):
                        tmp[c][level - r - 1] = a[i + r][j + c]
                for r in range(level):
                    a[i + r][j:j + level] = tmp[r]
    elif k == 4:
        ''' 4. 각 부분 배열을 왼쪽으로 90도 회전 '''
        for i in range(0, a_size, level):
            for j in range(0, a_size, level):
                tmp = [[0] * level for _ in range(level)]
                for r in range(level):
                    for c in range(level):
                        tmp[level - c - 1][r] = a[i + r][j + c]
                for r in range(level):
                    a[i + r][j:j + level] = tmp[r]
    elif k == 5:
        ''' 5. 배열 상하 반전 '''
        for i in range(0, a_size // 2, level):
            for r in range(level):
                a[i + r], a[-level - i + r] = a[-level - i + r], a[i + r]
    elif k == 6:
        ''' 6. 배열 좌우 반전 '''
        for i in range(a_size):
            for j in range(0, a_size // 2, level):
                a[i][j:j + level], a[i][a_size - level - j:a_size - j]\
                    = a[i][a_size - level - j:a_size - j], a[i][j:j + level]
    elif k == 7:
        ''' 7. 배열 오른쪽 90도 회전 '''
        tmp = [[0] * a_size for _ in range(a_size)]
        for i in range(0, a_size, level):
            for j in range(0, a_size, level):
                for r in range(level):
                    tmp[j + r][a_size - level - i:a_size - i] = a[i + r][j:j + level]
        a = tmp
    elif k == 8:
        ''' 8. 배열 왼쪽 90도 회전 '''
        tmp = [[0] * a_size for _ in range(a_size)]
        for i in range(0, a_size, level):
            for j in range(0, a_size, level):
                for r in range(level):
                    tmp[a_size - level - j + r][i:i + level] = a[i + r][j:j + level]
        a = tmp


for item in a:
    print(*item)
