import sys

s = str(sys.stdin.readline())
ans = 1
for i in range(len(s) - 1):
    if i > 0 and s[i] == s[i - 1]:
        c, d = 25, 9
    else:
        c, d = 26, 10

    if s[i] == "c":
        ans *= c
    else:
        ans *= d

print(ans)
