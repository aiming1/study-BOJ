import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
order = list(map(int, input().split()))
dice = [0] * 7

'''
명령: 동쪽 1, 서쪽 2, 북쪽 3, 남쪽 4
횡단면 이동 시: 1, 3, 6, 5번 자리가 +- 1
종단면 이동 시: 1, 2, 6, 4번 자리가 +- 1
'''

now_dice = [1, 3]  # (1의 위치, 3의 위치)
lr = [1, 3, 6, 5]
ud = [1, 2, 6, 4]
now_locate = [x, y]  # 현재 주사위 위치
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for item in order:
    if 0 <= now_locate[0] + dx[item] < n and 0 <= now_locate[1] + dy[item] < m:
        now_locate = [now_locate[0] + dx[item], now_locate[1] + dy[item]]
        if item == 1:  # 동쪽 이동 : lr + 1
            for i in range(2):
                for j in range(4):
                    if now_dice[i] == lr[j]:
                        now_dice[i] = lr[(j + 1) % 4]
                        break
        elif item == 2:  # 서쪽 이동 : lr - 1
            for i in range(2):
                for j in range(4):
                    if now_dice[i] == lr[j]:
                        now_dice[i] = lr[(j - 1) % 4]
                        break
        elif item == 3:  # 북쪽 이동 : ud - 1
            for i in range(2):
                for j in range(4):
                    if now_dice[i] == ud[j]:
                        now_dice[i] = ud[(j - 1) % 4]
                        break
        else:  # 남쪽 이동 : ud + 1
            for i in range(2):
                for j in range(4):
                    if now_dice[i] == ud[j]:
                        now_dice[i] = ud[(j + 1) % 4]
                        break

        if now_dice[0] == 1:  # 1이 윗면인 경우
            if board[now_locate[0]][now_locate[1]] == 0:
                board[now_locate[0]][now_locate[1]] = dice[6]
            else:
                dice[6] = board[now_locate[0]][now_locate[1]]
                board[now_locate[0]][now_locate[1]] = 0
            print(dice[1])
        elif now_dice[0] == 6:  # 6이 윗면인 경우
            if board[now_locate[0]][now_locate[1]] == 0:
                board[now_locate[0]][now_locate[1]] = dice[1]
            else:
                dice[1] = board[now_locate[0]][now_locate[1]]
                board[now_locate[0]][now_locate[1]] = 0
            print(dice[6])
        elif now_dice[1] == 1:  # 3이 윗면인 경우
            if board[now_locate[0]][now_locate[1]] == 0:
                board[now_locate[0]][now_locate[1]] = dice[4]
            else:
                dice[4] = board[now_locate[0]][now_locate[1]]
                board[now_locate[0]][now_locate[1]] = 0
            print(dice[3])
        elif now_dice[1] == 6:  # 4가 윗면인 경우
            if board[now_locate[0]][now_locate[1]] == 0:
                board[now_locate[0]][now_locate[1]] = dice[3]
            else:
                dice[3] = board[now_locate[0]][now_locate[1]]
                board[now_locate[0]][now_locate[1]] = 0
            print(dice[4])
        elif (now_dice[0] == 2 and now_dice[1] == 3) or (now_dice[0] == 3 and now_dice[1] == 4)\
                or (now_dice[0] == 4 and now_dice[1] == 5) or (now_dice[0] == 5 and now_dice[1] == 2):
            # 2가 윗면인 경우
            if board[now_locate[0]][now_locate[1]] == 0:
                board[now_locate[0]][now_locate[1]] = dice[5]
            else:
                dice[5] = board[now_locate[0]][now_locate[1]]
                board[now_locate[0]][now_locate[1]] = 0
            print(dice[2])
        elif (now_dice[0] == 3 and now_dice[1] == 2) or (now_dice[0] == 4 and now_dice[1] == 3) \
                or (now_dice[0] == 5 and now_dice[1] == 4) or (now_dice[0] == 2 and now_dice[1] == 5):
            # 5가 윗면인 경우
            if board[now_locate[0]][now_locate[1]] == 0:
                board[now_locate[0]][now_locate[1]] = dice[2]
            else:
                dice[2] = board[now_locate[0]][now_locate[1]]
                board[now_locate[0]][now_locate[1]] = 0
            print(dice[5])
