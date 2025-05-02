import sys

input = sys.stdin.readline

n, l = map(int, input().split())

while l <= 100:
    if l % 2 == 1 and (n / (1 + 2 * (l // 2))) == (n // (1 + 2 * (l // 2))):
            x = n // (1 + 2 * (l // 2))
            if x - l // 2 >= 0:
                print(*list(i for i in range(x - l // 2, x + l // 2 + 1)))
                sys.exit()
    elif l % 2 == 0 and n / (2 * (l // 2)) - n // (2 * (l // 2)) == 0.5:
        x = int(n / (2 * (l // 2)) - 0.5)
        if x - l // 2 + 1 >= 0:
            print(*list(i for i in range(x - l // 2 + 1, x + l // 2 + 1)))
            sys.exit()
    l += 1

print(-1)
