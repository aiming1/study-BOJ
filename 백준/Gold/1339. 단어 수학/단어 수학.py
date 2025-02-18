import sys

input = sys.stdin.readline

n = int(input())
alphabet = [0] * 26
for _ in range(n):
    word = str(input())[:-1]
    length = len(word) - 1
    for spell in word:
        alphabet[ord(spell) - 65] += 10 ** length
        length -= 1
alphabet.sort(reverse=True)

ans = 0
i, num = 0, 9
while alphabet[i] != 0:
    ans += alphabet[i] * num
    i += 1
    num -= 1

print(ans)
