import copy
import sys

input = sys.stdin.readline

''' 입력 '''
n, m, r = map(int, input().split())
input_array = list()
for _ in range(n):
    input_array.append(list(map(int, input().split())))
cal = list(map(int, input().split()))

''' 로직 '''
def one(array):  # 1. 배열 상하 반전
    array.reverse()
    res = copy.deepcopy(array)
    array.reverse()
    return res


def two(array):  # 2. 배열 좌우 반전
    res = []
    for row in array:
        row.reverse()
        res.append(copy.deepcopy(row))
        row.reverse()
    return res


def three(array):  # 3. 오른쪽 90도 회전
    res = []
    tmp = []
    for i in range(m):
        for j in range(n - 1, -1, -1):
            tmp.append(array[j][i])
        res.append(copy.deepcopy(tmp))
        tmp.clear()
    return res


def four(array):  # 4. 왼쪽 90도 회전
    res = []
    tmp = []
    for i in range(m - 1, -1, -1):
        for j in range(n):
            tmp.append(array[j][i])
        res.append(copy.deepcopy(tmp))
        tmp.clear()
    return res


def five(array):  # 5. 1 -> 2, 2 -> 3, 3 -> 4, 4 -> 1
    res = []
    for item in array[:n // 2]:  # 1 -> 2
        res.append(item[:m // 2])
    for i in range(n // 2):  # 4 -> 1
        res[i] = array[n // 2 + i][:m // 2] + res[i]
    for item in array[n // 2:]:  # 3 -> 4
        res.append(item[m // 2:])
    for i in range(n // 2):  # 2 -> 3
        res[n // 2 + i] = res[n // 2 + i] + array[i][m // 2:]
    return res


def six(array):  # 6. 1 -> 4, 4 -> 3, 3 -> 2, 2 -> 1
    res = []
    for item in array[:n // 2]:  # 2 -> 1
        res.append(item[m // 2:])
    for i in range(n // 2):  # 3 -> 2
        res[i] = res[i] + array[n // 2 + i][m // 2:]
    for item in array[:n // 2]:  # 1 -> 4
        res.append(item[:m // 2])
    for i in range(n // 2):  # 4 -> 3
        res[n // 2 + i] = res[n // 2 + i] + array[n // 2 + i][:m // 2]
    return res


for c in cal:
    if c == 1:
        input_array = one(input_array)
    elif c == 2:
        input_array = two(input_array)
    elif c == 3:
        input_array = three(input_array)
        n, m = m, n
    elif c == 4:
        input_array = four(input_array)
        n, m = m, n
    elif c == 5:
        input_array = five(input_array)
    elif c == 6:
        input_array = six(input_array)

for item in input_array:
    print(*item)
