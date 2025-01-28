import sys

input = sys.stdin.readline
color = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6,\
             'violet': 7, 'grey': 8, 'white': 9}

ans = 0
for i in range(3):
    c = str(input())[:-1]
    if i != 2:
        ans = ans * 10 + color[c]
    else:
        ans = ans * (10 ** color[c])

print(ans)
