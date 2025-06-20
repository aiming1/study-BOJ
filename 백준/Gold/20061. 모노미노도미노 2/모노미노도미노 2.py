import sys

input = sys.stdin.readline

green = [[0] * 4 for _ in range(6)]
blue = [[0] * 6 for _ in range(4)]

def find_borderline():
    g, b = [6] * 4, [6] * 4
    for i in range(2, 6):
        for j in range(4):
            if green[i][j] == 1 and g[j] == 6:
                g[j] = i
            if blue[j][i] == 1 and b[j] == 6:
                b[j] = i
    return g, b

def new_block(t, x, y):
    global green, blue

    greenBorderline, blueBorderline = find_borderline()
    if t == 1:
        green[greenBorderline[y] - 1][y] = 1
        blue[x][blueBorderline[x] - 1] = 1
    elif t == 3:
        green[greenBorderline[y] - 2][y] = 1
        green[greenBorderline[y] - 1][y] = 1
        blue[x][min(blueBorderline[x], blueBorderline[x + 1]) - 1] = 1
        blue[x + 1][min(blueBorderline[x], blueBorderline[x + 1]) - 1] = 1
    elif t == 2:
        green[min(greenBorderline[y], greenBorderline[y + 1]) - 1][y] = 1
        green[min(greenBorderline[y], greenBorderline[y + 1]) - 1][y + 1] = 1
        blue[x][blueBorderline[x] - 2] = 1
        blue[x][blueBorderline[x] - 1] = 1

def make_score(obj):
    global score

    for i in range(6):
        if obj[i] == [1, 1, 1, 1]:
            score += 1
        else:
            obj.append(obj[i])
    obj = obj[6:]
    obj = [[0] * 4 for _ in range(len(obj), 6)] + obj

    return obj

def reverse_list(l, clockwise = True):
    if clockwise:
        return list(map(list, zip(*l[::-1])))
    else:
        return list(map(list, zip(*l)))[::-1]


def chk_01(obj):
    delete_cnt = 0

    for i in range(2):
        if obj[i] != [0, 0, 0, 0]:
            delete_cnt += 1

    if delete_cnt != 0:
        obj = obj[:-delete_cnt]
        obj = [[0] * 4 for _ in range(delete_cnt)] + obj

    return obj

def count_tile():
    global green, blue

    result = 0

    for obj in (green, reverse_list(blue)):
        for line in obj:
            result += sum(line)

    return result


''' main '''
n = int(input())
score = 0
for _ in range(n):
    t, x, y = map(int, input().split())
    new_block(t, x, y)

    # print("=== new block ===")
    # for line in green:
    #     print(line)
    # print("----")
    # for line in blue:
    #     print(line)
    # print("")

    green = make_score(green)
    blue = reverse_list(make_score(reverse_list(blue)), clockwise=False)

    # print("=== make score ===")
    # for line in green:
    #     print(line)
    # print("----")
    # for line in blue:
    #     print(line)
    # print("")

    green = chk_01(green)
    blue = reverse_list(chk_01(reverse_list(blue)), clockwise=False)

    # print("=== chk zero one line ===")
    # for line in green:
    #     print(line)
    # print("----")
    # for line in blue:
    #     print(line)
    # print("")


print(score)
print(count_tile())
