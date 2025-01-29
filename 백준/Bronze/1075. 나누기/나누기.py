import sys

input = sys.stdin.readline

n = int(input())
f = int(input())

nn = n // 100 * 100
for i in range(100):
    if (nn + i) % f == 0:
        print("%02d" % i)
        break
