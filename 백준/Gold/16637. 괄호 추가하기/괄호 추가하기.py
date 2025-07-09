import copy
import sys
from collections import deque

input = sys.stdin.readline

n, formula = int(input()), list(str(input()))
for i in range(0, n, 2):
    formula[i] = int(formula[i])

def calculator(x, a, b):
    if formula[x] == '+':
        return a + b
    elif formula[x] == '-':
        return a - b
    else:
        return a * b

if n == 1:
    print(formula[0])
    exit()

next_queue = deque([(calculator(1, formula[0], formula[2]), formula[0], 0)])

for i in range(3, n, 2):
    queue = copy.deepcopy(next_queue)
    next_queue = deque()
    while queue:
        calculated, bf_calculated, oploc = queue.popleft()
        # 주어진 수에 그냥 연산하기
        next_queue.append([calculator(i, calculated, formula[i + 1]), calculated, oploc])
        # 새 괄호 적용하기
        if i > oploc + 2:
            next_queue.append([calculator(i - 2, bf_calculated, calculator(i, formula[i - 1], formula[i + 1])), calculated, i])

print(max(next_queue)[0])
