import copy
import sys
from collections import deque

input = sys.stdin.readline

board = [''] * 3  # 인풋 보드
final_board = {'A': '', 'B': '', 'C': ''}  # 완성된 보드의 모양새
for i in range(3):
    s = list(map(str, input().split()))
    if s[0] != '0':
        board[i] = s[1]
        for item in board[i]:
            final_board[item] = final_board[item] + item


def make_key(chk):
    return chk[0] + '/' + chk[1] + '/' + chk[2]


def check_ans(b):
    for key in ('A', 'B', 'C'):
        if final_board[key] != b[ord(key) - 65]:
            return False
    return True


def bfs(start):
    visited = {make_key(start)}
    queue = deque([(start, 0)])
    while queue:
        now_board, cnt = queue.popleft()
        if check_ans(now_board):
            return cnt

        for i in range(3):
            if len(now_board[i]) == 0:
                continue
            for dir in (-1, -2):
                new_board = copy.deepcopy(now_board)
                new_board[i + dir] = new_board[i + dir] + new_board[i][-1]
                new_board[i] = new_board[i][:-1]
                new_key = make_key(new_board)
                if new_key not in visited:
                    queue.append([new_board, cnt + 1])
                    visited.add(new_key)


print(bfs(board))
