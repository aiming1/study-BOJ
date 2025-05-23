import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
a = list()
for _ in range(n):
    a.append(list(map(int, input().split())))
tree = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)
nutri = [[5] * n for _ in range(n)]
d = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

for ty in range(k):
    for i in range(n):
        for j in range(n):
            if len(tree[i][j]):
                tree[i][j].sort()
                ''' 봄 : 나이만큼 양분을 먹고 나이가 1 증가 '''
                for p in range(0, len(tree[i][j])):
                    if nutri[i][j] >= tree[i][j][p]:  # 나무가 양분을 먹을 수 있으면
                        nutri[i][j] -= tree[i][j][p]  # 양분을 먹고
                        tree[i][j][p] += 1  # 나무 나이 +1
                    else:  # 나무가 양분을 먹을 수 없으면
                        die = p  # 해당(p번째) 나무부터는 죽는다
                        break
                else:  # 모든 나무가 양분을 먹고 넘어갔다면
                    die = len(tree[i][j])  # 죽는 나무 없음

                ''' 여름 : 죽은 나무가 양분으로 변한다, 변하는 값은 나무의 나이 // 2 '''
                for p in range(die, len(tree[i][j])):  # 죽는 나무 없을 경우: 반복문 실행 X
                    nutri[i][j] += tree[i][j][p] // 2
                if die != 0:
                    tree[i][j] = tree[i][j][:die]  # 죽은 나무들은 나무 리스트에서 탈락
                else:  # 모든 나무가 죽을 경우
                    tree[i][j] = []

    ''' 가을 : 나이가 5의 배수인 나무가 번식 '''
    for i in range(n):
        for j in range(n):
            if len(tree[i][j]):
                for t in tree[i][j]:
                    if t % 5 == 0:  #  나이가 5의 배수인 나무에 한해서 번식
                        for dx, dy in d:
                            nx, ny = i + dx, j + dy
                            if 0 <= nx < n and 0 <= ny < n:  # 번식 가능한 칸이면
                                tree[nx][ny].append(1)  # 해당 칸에 번식 - 나이가 1인 나무가 생김

    ''' 겨울 : a에 저장되어 있던 양분을 땅에 추가 '''
    for i in range(n):
        for j in range(n):
            nutri[i][j] += a[i][j]


''' K년이 지난 후 : 살아 있는 나무의 개수 구하기 '''
ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree[i][j])

print(ans)
