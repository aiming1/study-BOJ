from collections import deque


N, K = map(int, input().split())
MAX = 100001
move = [-1] * MAX	# 이전 경로를 저장하는 배열
move[N] = N
answer = []
q = deque([N])

while q:
    cur = q.popleft()
    if cur == K:
        while cur != N:     	# 인덱스 값이 N인 경우, 도착한 것이니 종료
            answer.append(cur)	# 경로에 추가
            cur = move[cur]		# 현재 위치를 이전 위치로 갱신
        answer.append(N)
        break
    for m in (cur-1, cur+1, cur << 1):
        if 0 <= m < MAX and move[m] == -1:
            move[m] = cur
            q.append(m)

print(len(answer)-1)
print(*answer[::-1])