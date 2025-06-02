n, m = map(int, input().split())
bucket = [[0] for _ in range(n + 1)]
for _ in range(m):
    a, b, k = map(int, input().split())
    for i in range(a, b + 1):
        bucket[i].append(k)
for item in bucket[1:]:
    print(item[-1], end = " ")