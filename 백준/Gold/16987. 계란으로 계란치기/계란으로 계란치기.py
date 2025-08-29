import sys

input = sys.stdin.readline

n = int(input())
eggs_durability = list()  # 내구도 배열
eggs_weight = list()  # 무게 배열
for _ in range(n):
    a, b = map(int, input().split())
    eggs_durability.append(a)
    eggs_weight.append(b)

''' 깨진 달걀 개수 세기 '''
def cnt_ans(this_eggs):
    cnt = 0
    for egg in this_eggs:
        if egg <= 0:
           cnt += 1
    return cnt

def dfs(now, this_eggs):
    global ans

    ''' 계란을 다 한 번씩 들었다 놨거나 남은 계란이 하나뿐이면 탐색 끝'''
    if now >= n or cnt_ans(this_eggs) == n - 1:
        ans.add(cnt_ans(this_eggs))
        return

    ''' 든 계란이 깨졌을 경우, 든 계란이 맨 마지막 계란이면 탐색 끝, 아니면 다음 계란 듦 '''
    if this_eggs[now] <= 0:  # 든 계란이 깨진 계란
        while this_eggs[now] <= 0:
            if now == n - 1:
                ans.add(cnt_ans(this_eggs))
                return
            now += 1

    for i in range(n):
        ''' 손에 든 계란 != 깨려고 하는 계란
            깨려고 하는 계란 != 이미 깨진 계란
            일 때 다음 탐색 '''
        if now != i and this_eggs[i] > 0:
            this_eggs[now] -= eggs_weight[i]
            this_eggs[i] -= eggs_weight[now]
            dfs(now + 1, this_eggs)
            this_eggs[now] += eggs_weight[i]
            this_eggs[i] += eggs_weight[now]

ans = set()
dfs(0, eggs_durability)
print(max(ans))
