import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [[[0, 0] for _ in range(n)] for _ in range(n)]
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(n):
        if l[j] != 0:
            board[i][j] = [l[j], k]
sharks = [0] + list(map(int, input().split()))
priority = [[0] * 5 for _ in range(m + 1)]
for i in range(1, m + 1):
    for j in range(1, 5):
        priority[i][j] = list(map(int, input().split()))
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
'''
    board[x][y] : (x, y) 위치의 [흔적 번호, 남은 시간] 
    sharks[n] : n번 상어 방향
    priority[n][d] : n번 상어가 d 방향일 때 우선순위
'''

''' 움직일 수 있는 상어 좌표 찾기
    반환: 상어들의 좌표를 담은 리스트 '''
def find_movable_shark():
    result = list()
    for i in range(n):
        for j in range(n):
            if board[i][j][1] == k:
                result.append([i, j])
    return result

''' 매개변수 좌표의 상어가 움직일 칸 찾기
    반환: 상어가 움직일 방향 '''
def find_next_dir(x, y):
    movable_dirs = [[] for _ in range(2)]  # [0]: 아무 냄새 X [1]: 본인 냄새
    shark = board[x][y][0]  # 움직일 상어
    dir = sharks[shark]  # 그 상어가 가지고 있는 방향
    for i in range(1, 5):  # 이동 가능한 칸 전부 찾기
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny][0] == 0:
                movable_dirs[0].append(i)
            elif board[nx][ny][0] == shark:
                movable_dirs[1].append(i)

    this_priority = priority[shark][dir]  # 상어 이동방향 우선순위
    for i in range(2):  # 이동할 칸 우선순위 맞게 찾기
        for p in this_priority:
            for item in movable_dirs[i]:
                if p == item:
                    return item
    return 0

''' 중복 상어 삭제
    반환: 삭제 후의 보드 '''
def delete_duplicate(this_board):
    for i in range(n):
        for j in range(n):
            if len(this_board[i][j]) > 1:  # 상어 여러 마리가 있는 경우
                this_board[i][j].sort()
                this_board[i][j] = this_board[i][j][0]
            elif len(this_board[i][j]) == 1:  # 상어 한 마리 있는 경우
                this_board[i][j] = this_board[i][j][0]
    return this_board

''' 냄새 남은 시간 조절
    반환: 조절 완료된 후의 보드 '''
def smell_ctrl(this_board):
    for i in range(n):
        for j in range(n):
            if k > board[i][j][1] > 0 and not this_board[i][j]:  # 조절이 필요한 경우
                this_board[i][j] = [board[i][j][0], board[i][j][1] - 1]
                if this_board[i][j][1] == 0:  # 냄새 사라져야 됨
                    this_board[i][j][0] = 0
    return this_board

''' 보드 빈 칸 채우기
    반환: 채워진 보드 '''
def fill_blank(this_board):
    for i in range(n):
        for j in range(n):
            if not this_board[i][j]:
                this_board[i][j] = [0, 0]
    return this_board


''' 상어 움직
    반환: 상어 이동이 완료된 후의 board '''
def move_sharks():
    new_board = [[[] for _ in range(n)] for _ in range(n)]
    obj = find_movable_shark()  # 움직일 상어들 찾기
    for x, y in obj:  # 상어 한 마리씩 반복
        this_shark = board[x][y][0]  # 이번에 움직일 상어 번호
        d = find_next_dir(x, y)  # 움직일 방향 찾기
        sharks[this_shark] = d  # 상어 방향 DB 수정
        nx, ny = x + dx[d], y + dy[d]  # 이동할 좌표 설정
        new_board[nx][ny].append([this_shark, k])  # 이동
        if k != 1:
            new_board[x][y].append([this_shark, k - 1])  # 있던 곳에는 본인의 냄새를 뿌린다

    new_board = delete_duplicate(new_board)  # 이동 후 칸에 중복된 상어 삭제
    new_board = smell_ctrl(new_board)  # 냄새 남은 횟수 조절
    new_board = fill_blank(new_board)  # [0, 0] 채우기
    return new_board

''' 종료 조건 체크 '''
def chk_exit():
    if len(find_movable_shark()) == 1:
        return True
    return False

for t in range(1, 1001):
    board = move_sharks()  # 상어 이동
    if chk_exit():  # 종료 조건 체크
        print(t)
        exit()

print(-1)
