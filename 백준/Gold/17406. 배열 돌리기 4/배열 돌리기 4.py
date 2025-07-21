import copy
import sys
from itertools import combinations, permutations

input = sys.stdin.readline

n, m, k = map(int, input().split())
a = list()
for _ in range(n):
    a.append(list(map(int, input().split())))
rotations = list()
for _ in range(k):
    A, B, C = map(int, input().split())
    rotations.append([A - 1, B - 1, C])


def rotate(r, c, s, board):
    rotate_done = [[0] * m for _ in range(n)]
    rotate_done[r][c] = board[r][c]
    for ss in range(1, s + 1):
        rotate_done[r - ss][c - ss:c + ss] = ([board[r - ss + 1][c - ss]] + board[r - ss][c - ss:c + ss])[:-1]
        rotate_done[r - ss][c + ss] = board[r - ss][c + ss - 1]
        for i in range(r - ss + 1, r + ss):
            rotate_done[i][c + ss] = board[i - 1][c + ss]
        rotate_done[r + ss][c + ss] = board[r + ss - 1][c + ss]
        for i in range(c + ss - 1, c - ss, - 1):
            rotate_done[r + ss][i] = board[r + ss][i + 1]
        rotate_done[r + ss][c - ss] = board[r + ss][c - ss + 1]
        for i in range(r + ss - 1, r - ss, -1):
            rotate_done[i][c - ss] = board[i + 1][c - ss]
    for i in range(r - s, r + s + 1):
        board[i][c - s:c + s + 1] = rotate_done[i][c - s:c + s + 1]

def getvalue(board):
    min_sum = sum(board[0])
    for i in range(1, n):
        min_sum = min(min_sum, sum(board[i]))
    return min_sum

ans = float('inf')
for combi in permutations(rotations, len(rotations)):
    board = copy.deepcopy(a)
    for r, c, s in combi:
        rotate(r, c, s, board)
    ans = min(ans, getvalue(board))

print(ans)
