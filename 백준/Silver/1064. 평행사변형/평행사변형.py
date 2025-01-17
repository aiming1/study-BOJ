import sys

input = sys.stdin.readline

xa, ya, xb, yb, xc, yc = map(int, input().split())

if xa == xb == xc or ya == yb == yc:
    print(-1)
    sys.exit()
elif xb - xa != 0 and xc - xa != 0:
    if (yb - ya) / (xb - xa) == (yc - ya) / (xc - xa):
        print(-1)
        sys.exit()

square = [(((xa - xb) ** 2 + (ya - yb) ** 2) ** (1 / 2) + ((xa - xc) ** 2 + (ya - yc) ** 2) ** (1 / 2)) * 2,
          (((xa - xb) ** 2 + (ya - yb) ** 2) ** (1 / 2) + ((xc - xb) ** 2 + (yc - yb) ** 2) ** (1 / 2)) * 2,
          (((xa - xc) ** 2 + (ya - yc) ** 2) ** (1 / 2) + ((xc - xb) ** 2 + (yc - yb) ** 2) ** (1 / 2)) * 2]

print(abs(max(square) - min(square)))
