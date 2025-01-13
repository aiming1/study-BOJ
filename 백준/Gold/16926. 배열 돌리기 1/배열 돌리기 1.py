import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
input_array = [[0] * (m + 1)]
for _ in range(n):
    input_array.append([0] + list(map(int, input().split())))


def rotation(ori_array):
    new_array = [[0] * (m + 1) for _ in range(n + 1)]
    for rotate in range(1, min(n, m) // 2 + 1):
        for i in range(rotate, n - rotate + 2):
            if i == rotate:  # 상
                for j in range(rotate, m - rotate + 1):
                    new_array[i][j] = ori_array[i][j + 1]
                new_array[i][m - rotate + 1] = ori_array[i + 1][m - rotate + 1]
            elif i == n - rotate + 1:  # 하
                new_array[i][rotate] = ori_array[i - 1][rotate]
                for j in range(rotate + 1, m - rotate + 2):
                    new_array[i][j] = ori_array[i][j - 1]
            else:  # 좌, 우
                new_array[i][rotate] = ori_array[i - 1][rotate]
                new_array[i][m - rotate + 1] = ori_array[i + 1][m - rotate + 1]

    return new_array


for cnt in range(r):
    input_array = rotation(input_array)


for item in input_array[1:]:
    print(*item[1:])
