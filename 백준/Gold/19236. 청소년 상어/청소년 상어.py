import copy
import sys

input = sys.stdin.readline

fishes = [[] for _ in range(4)]
for i in range(4):
    l = list(map(int, input().split()))
    for j in range(0, 8, 2):
        fishes[i].append([l[j], l[j + 1] - 1])
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

ans = list()

def find_fish(this_fishes, num):  # num번 물고기가 살아 있는지 확인 -> 좌표 리턴
    for i in range(4):
        for j in range(4):
            if this_fishes[i][j][0] == num:
                return i, j
    return -1, -1

def move_fish(this_fishes):  # 전체 물고기 이동
    for num in range(1, 17):
        x, y = find_fish(this_fishes, num)  # 이동 물고기 좌표
        if x == -1:  # 해당 물고기 사망 시 패스
            continue

        d = this_fishes[x][y][1]  # 이동 물고기 초기 방향

        for i in range(8):
            nx, ny = x + dx[(d + i) % 8], y + dy[(d + i) % 8]
            if 0 <= nx < 4 and 0 <= ny < 4 and this_fishes[nx][ny][0] != -1:  # 이동 가능
                this_fishes[x][y][1] = (d + i) % 8
                this_fishes = swap_fish_loc(x, y, nx, ny, this_fishes)
                break

    return this_fishes

def swap_fish_loc(x, y, nx, ny, this_fishes):  # (x, y) <-> (nx, ny)
    this_fishes[x][y], this_fishes[nx][ny]\
        = [this_fishes[nx][ny][0], this_fishes[nx][ny][1]], [this_fishes[x][y][0], this_fishes[x][y][1]]
    return this_fishes

def dfs(this_fishes, size, x, y, d):
    ''' 상어 위치 체크 '''
    this_fishes[x][y][0] = -1

    ''' 물고기 이동 '''
    this_fishes = move_fish(this_fishes)

    ''' 상어 이동 '''
    for i in range(1, 4):
        nx, ny = x + dx[d] * i, y + dy[d] * i  # 상어 -> 방향 맞으면 몇 칸이든 이동 가능
        if 0 <= nx < 4 and 0 <= ny < 4 and this_fishes[nx][ny][0] != 0:# 이동 O
            this_fishes[x][y][0] = 0  # 상어는 있던 곳을 떠난다
            dfs(copy.deepcopy(this_fishes), size + this_fishes[nx][ny][0], nx, ny, this_fishes[nx][ny][1])

    ans.append(size)  # 위의 루프 다 끝 -> 더는 상어가 이동할 곳 X

dfs(fishes, fishes[0][0][0], 0, 0, fishes[0][0][1])

print(max(ans))
