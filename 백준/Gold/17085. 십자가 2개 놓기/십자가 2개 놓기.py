import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board, blank = list(), 0
for _ in range(n):
    board.append(str(input())[:-1])
    for s in board[-1]:
        if s == '#':
            blank += 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

''' [x, y] 좌표에 크기가 1 이상인 십자가를 놓을 수 있는지 체크 '''
def check_cross_able(x, y, visited=None):
    if board[x][y] == '.':
        return False
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0 <= nx < n) or not (0 <= ny < m)\
            or board[nx][ny] == '.':
            return False
        if visited and (nx, ny) in visited:
            return False
    return True

''' [x, y] 좌표에 놓는 것이 가능한 사이즈 get '''
def get_size_set(x, y, visited=None):
    size = {1}
    for i in range(2, 8):
        for j in range(4):
            nx, ny = x + dx[j] * i, y + dy[j] * i
            if not (0 <= nx < n) or not (0 <= ny < m)\
                or board[nx][ny] == '.':
                return size
            if visited and (nx, ny) in visited:
                return size
        size.add(i)
    return size

def get_next_cross(x, y, visited):
    size = {0}

    for j in range(y + 1, m):  # x번째 행
        if check_cross_able(x, j, visited):
            size = size | get_size_set(x, j, visited)
    for i in range(x + 1, n):  # x번째 행 이후
        for j in range(m):
            if check_cross_able(i, j, visited):
                size = size | get_size_set(i, j, visited)

    return max(size) * 4 + 1

def create_visited(x, y, e):
    visited = set()
    for s in range(e + 1):
        for a in range(4):
            nx, ny = x + dx[a] * s, y + dy[a] * s
            visited.add((nx, ny))
    return visited


''' 크기가 0인 십자가 두 개는 무조건 가능성이 성립하므로 시뮬레이션에서 제외 '''
ans = {1}
for i in range(n):
    for j in range(m):
        if check_cross_able(i, j):  # 크기가 1 이상인 십자가를 놓을 수 있음
            sizes = get_size_set(i, j)
            for element in sizes:
                if blank == element * 4 + 1:
                    continue
                ans.add(get_next_cross(i, j, create_visited(i, j, element)) * (4 * element + 1))
print(max(ans))