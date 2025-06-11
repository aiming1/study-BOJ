import sys

input = sys.stdin.readline

n, x = map(int, input().split())
layer, patty = [1] * 51, [1] * 51
for i in range(1, 51):
    layer[i] = 3 + 2 * layer[i - 1]
    patty[i] = 1 + 2 * patty[i - 1]
eat_level, eat_pt = n - 1, x

ans = 0
while eat_pt > 0:  # 먹을 양이 남아 있는 동안 반복
    ''' eat_level == 0인 경우 BLPLB 구조는 BPPPB로 수렴 '''
    if eat_level == 0:
        print(ans - 1 + (eat_pt if eat_pt <= 4 else 4))
        exit()

    ''' [B]LPLB '''
    eat_pt -= 1

    ''' B[L]PLB '''
    if eat_pt >= layer[eat_level]:  # 다음으로 주어진 레벨 전체를 먹을 수 있는 경우
        ans += patty[eat_level]
        eat_pt -= layer[eat_level]
        eat_level -= 1

        ''' BL[P]LB '''
        if eat_pt > 0:
            eat_pt -= 1
            ans += 1

    else:  # 다음으로 주어진 레벨 전체를 먹을 수 없는 경우
        eat_level -= 1


    ''' BLP[L]B: 이 L은 전 단계 레벨에 대해 BLPLB 구조를 가지므로 사이클 반복 '''

print(ans)
