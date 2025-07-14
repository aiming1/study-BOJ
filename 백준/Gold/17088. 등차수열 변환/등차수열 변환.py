import sys

input = sys.stdin.readline

n, b = int(input()), list(map(int, input().split()))
ans = set()

if n <= 2:
    print(0)
    exit()

for a in (-1, 0, 1):
    start = b[0] + a
    for aa in (-1, 0, 1):
        comp, cnt = b[1] + aa, abs(a) + abs(aa)
        diff = comp - start

        for i in range(2, n):
            continue_Flag = False
            for op in (-1, 0, 1):
                if b[i] + op - comp == diff:
                    comp = b[i] + op
                    cnt += abs(op)
                    continue_Flag = True
                    break
            if not continue_Flag:
                break
        else:
            ans.add(cnt)

print(min(ans) if len(ans) else -1)

