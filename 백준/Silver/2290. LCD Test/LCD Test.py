import sys

input = sys.stdin.readline

s, n = map(int, input().split())
n = str(n)
line = ''

''' 1번 '''
for num in n:
    if num == "1" or num == "4":
        line = line + ' ' * (s + 2) + ' '
    else:
        line = line + ' ' + '-' * s + ' ' + ' '
print(line)
line = ''

''' 2번 '''
for num in n:
    if num == "4" or num == "8" or num == "9" or num == "0":
        line = line + '|' + ' ' * s + '|' + ' '
    elif num == "1" or num == "2" or num == "3" or num == "7":
        line = line + ' ' * (s + 1) + '|' + ' '
    else:
        line = line + '|' + ' ' * (s + 1) + ' '
for _ in range(s):
    print(line)
line = ''

''' 3번 '''
for num in n:
    if num == "1" or num == "7" or num == "0":
        line = line + ' ' * (s + 2) + ' '
    else:
        line = line + ' ' + '-' * s + ' ' + ' '
print(line)
line = ''

''' 4번 '''
for num in n:
    if num == "6" or num == "8" or num == "0":
        line = line + '|' + ' ' * s + '|' + ' '
    elif num == "1" or num == "3" or num == "4" or num == "5" or num == "7" or num == "9":
        line = line + ' ' * (s + 1) + '|' + ' '
    else:
        line = line + '|' + ' ' * (s + 1) + ' '
for _ in range(s):
    print(line)
line = ''

''' 5번 '''
for num in n:
    if num == "1" or num == "4" or num == "7":
        line = line + ' ' * (s + 2) + ' '
    else:
        line = line + ' ' + '-' * s + ' ' + ' '
print(line)
