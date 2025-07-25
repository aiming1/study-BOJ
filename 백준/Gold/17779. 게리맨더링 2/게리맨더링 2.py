import sys

input = sys.stdin.readline

n = int(input())
a = list()
sum_all = 0
for _ in range(n):
    a.append(list(map(int, input().split())))
    sum_all += sum(a[-1])

def get_population_diff(tx, ty, td1, td2):
    global a

    cnt_set = list()
    cor = [[tx, ty, td1, td2],
           [ty - td1, n - (tx + td1 + 1), td2, td1],
           [n - (tx + td1 + td2 + 1), n - (ty - td1 + td2 + 1), td1, td2],
           [n - (ty + td2 + 1), tx + td2, td2, td1]]

    for turn in range(4):
        tx, ty, td1, td2 = cor[turn]
        cnt = 0

        for i in range(tx):  # x행 위
            for j in range(ty + 1):
                cnt += a[i][j]

        for i in range(tx, tx + td1):
            for j in range(ty - (i - tx)):  # 1번 선거구
                cnt += a[i][j]
        cnt_set.append(cnt)

        a = list(zip(*a[::-1]))

    cnt_set.append(sum_all - sum(cnt_set))

    return max(cnt_set) - min(cnt_set)

ans = float('inf')
for x in range(n):
    for y in range(1, n - 1):
        ''' --- (x, y) 결정 --- '''
        for d1 in range(1, n - 1):
            if y - d1 < 0:  # 왼쪽 좌표 벗어남
                break
            for d2 in range(1, n - 1):
                if y + d2 >= n:  # 오른쪽 좌표 벗어남
                    break
                if x + d1 + d2 >= n:  # 아래 좌표 벗어남
                    break
                ans = min(ans, get_population_diff(x, y, d1, d2))

print(ans)
