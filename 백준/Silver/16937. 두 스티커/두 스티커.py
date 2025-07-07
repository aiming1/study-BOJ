import sys

input = sys.stdin.readline

h, w = map(int, input().split())
n = int(input())
stickers = list()
for _ in range(n):
    stickers.append(list(map(int, input().split())))

ans = {0}
for i in range(n):
    for j in range(i + 1, n):
        flag = False
        for H, W in [[h, w], [w, h]]:
            for ri, ci in [stickers[i], [stickers[i][1], stickers[i][0]]]:
                for rj, cj in [stickers[j], [stickers[j][1], stickers[j][0]]]:
                    if ((ri + rj) <= H and max(ci, cj) <= W) or ((ri + cj) <= H and max(rj, ci) <= W):
                        ans.add(ri * ci + rj * cj)
                        flag = True
                        break
                if flag:
                    break
            if flag:
                break

print(max(ans))


