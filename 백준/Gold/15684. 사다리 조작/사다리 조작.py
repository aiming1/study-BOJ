import sys
input = sys.stdin.readline

# 입력 받기
N, M, H = map(int, input().split())
ladder = [[-1] * N for _ in range(H)]  # 각 위치의 연결 정보를 저장 (-1은 연결 없음)

# 기존 가로선 정보 추가
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    ladder[a][b] = b + 1
    ladder[a][b + 1] = b

# 사다리 게임 결과 확인 함수
def check():
    for start in range(N):
        k = start  # 현재 위치
        for i in range(H):
            if ladder[i][k] != -1:
                k = ladder[i][k]  # 연결된 세로선으로 이동
        if k != start:
            return False
    return True

# 백트래킹을 이용한 가로선 추가 함수
def dfs(count, x, y):
    global min_count
    if count >= min_count:  # 가지치기: 현재까지의 가로선 수가 최소값 이상이면 종료
        return
    if check():
        min_count = count
        return
    if count == 3:  # 가로선을 3개까지 추가 가능
        return
    for i in range(x, H):
        k = y if i == x else 0
        for j in range(k, N - 1):
            if ladder[i][j] == -1 and ladder[i][j + 1] == -1:
                # 가로선 추가
                ladder[i][j] = j + 1
                ladder[i][j + 1] = j
                dfs(count + 1, i, j)
                # 가로선 제거 (백트래킹)
                ladder[i][j] = -1
                ladder[i][j + 1] = -1
        y = 0  # 다음 행부터는 y를 0으로 초기화

# 결과 출력
min_count = 4  # 가능한 최대 가로선 수 + 1로 초기화
dfs(0, 0, 0)
print(min_count if min_count <= 3 else -1)