import sys

input = sys.stdin.readline

n, m, t = map(int, input().split())
board = [[0]]
for _ in range(n):
    board.append(list(map(int, input().split())))
''' board[n] = [1, 2, 3, 4] 일 시 1부터 12시, 차례로 시계 방향 삽입 '''


def rotate(xi, clockwise, ki):  # 원판 회전
    global board

    if clockwise == 0:  # 시계 방향 회전
        board[xi] = board[xi][-ki:] + board[xi][:m - ki]
    else:  # 반시계 방향 회전
        board[xi] = board[xi][ki:] + board[xi][:ki]


def find_adj(xi):  # 인접한 같은 숫자 찾기
    global result

    for i in range(len(board[xi])):

        if board[xi][i] == 0:  # 삭제된 숫자는 패스
            continue

        for j in (1, -1):  # 같은 원판 내 양옆 체크
            comp = i + j if i + j < m else 0
            if board[xi][i] == board[xi][comp]:
                result[xi].add(comp)
                result[xi].add(i)
        if xi + 1 <= n:  # 위로 인접하는 원판이 존재하는 경우
            if board[xi][i] == board[xi + 1][i]:
                result[xi + 1].add(i)
                result[xi].add(i)
        if xi - 1 > 0:  # 아래로 인접하는 원판이 존재하는 경우
            if board[xi][i] == board[xi - 1][i]:
                result[xi - 1].add(i)
                result[xi].add(i)


def delete_num(obj):  # 숫자 삭제
    global board

    edit_obj = set()
    for key in obj.keys():
        if key == 0:  # 0번째 원반은 무효
            continue

        if not obj[key]:  # 탐색 중인 원반이 삭제할 것이 없는 원반인 경우
            edit_obj.add(key)
            continue

        for value in obj[key]:  # 탐색 중인 원반이 삭제할 것이 있는 경우 - 삭제
            board[key][value] = 0

    return True if len(edit_obj) != n else False


def edit_num():  # 지울 숫자가 없는 경우의 로직 함수
    global board

    board_len = 0
    board_sum = 0
    for line in board:
        for item in line:
            if item != 0:
                board_len += 1
        board_sum += sum(line)
    if board_len == 0:  # 원판의 모든 숫자가 삭제된 경우
        return
    avg = board_sum / board_len

    for i in range(1, n + 1):
        for j in range(m):
            if board[i][j] == 0:  # 삭제된 숫자는 패스
                continue

            if board[i][j] > avg:
                board[i][j] -= 1
            elif board[i][j] < avg:
                board[i][j] += 1



def get_sum():  # 원판에 적힌 수의 합 구하기
    result = 0
    for line in board:
        result += sum(line)
    return result


for a in range(t):
    x, d, k = map(int, input().split())
    for xi in range(x, n + 1, x):
        rotate(xi, d, k)

    result = {i:set() for i in range(1, n + 1)}  # 삭제할 수 모아 놓는 딕셔너리
    for x in range(1, n + 1):  # 숫자 찾기 과정은 전 원판에 대해 진행
        find_adj(x)  # 인접하면서 수가 같은 것을 모두 찾는다

    if delete_num(result):  # 지울 숫자들은 삭제
        continue
    else:  # 삭제할 숫자가 없어서 넘어갔다면
        edit_num()  # 편집

print(get_sum())
