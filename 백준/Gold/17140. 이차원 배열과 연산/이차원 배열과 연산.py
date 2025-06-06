import copy
import sys

input = sys.stdin.readline

def check(array):
    max_collen = 0
    for line in array:
        max_collen = max(max_collen, len(line))
    if len(array) >= max_collen:
        return "R"
    else:
        return "C"


def reverse_array(array):
    return list(zip(*array))


def R(array):
    max_linelen = 0
    for i in range(len(array)):
        num = [0] * 101  # num[n] : 숫자 n이 등장한 횟수
        for j in range(len(array[i])):
            num[array[i][j]] += 1

        count = {i:list() for i in range(1, 101)}  # count[n] : n번 등장한 숫자 모임
        for j in range(1, 101):
            if num[j] == 0:
                continue
            count[num[j]].append(j)

        new_line = list()  # 정렬 완료될 라인
        for key in count.keys():
            if count[key]:
                count[key].sort()
                for item in count[key]:
                    new_line.append(item)
                    new_line.append(key)

        array[i] = copy.deepcopy(new_line)
        max_linelen = max(max_linelen, len(new_line))

    for line in array:
        line += [0] * (max_linelen - len(line))

    return array


def C(array):
    array = R(reverse_array(array))
    return reverse_array(array)


r, c, k = map(int, input().split())
a = list()
for _ in range(3):
    a.append(list(map(int, input().split())))

for i in range(101):
    if len(a) >= r:
        if len(a[r - 1]) >= c:
            if a[r - 1][c - 1] == k:
                print(i)
                exit()

    if check(a) == "R":
        a = R(a)
    else:
        a = C(a)

print(-1)
